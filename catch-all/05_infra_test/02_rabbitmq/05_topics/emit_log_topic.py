#!/usr/bin/env python
import pika
import argparse
import logging
import time
import random
from datetime import datetime

# Configuración del logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def parse_arguments():
    """
    Analiza los argumentos de línea de comandos utilizando argparse.
    Devuelve un objeto con los argumentos proporcionados por el usuario.
    """

    parser = argparse.ArgumentParser(
        description='Enviar mensajes a un intercambio de tipo "topic" en RabbitMQ.')
    parser.add_argument(
        'routing_key', help='La clave de enrutamiento para el mensaje.')
    parser.add_argument(
        'message', nargs='*', default=['Hola', 'Mundo!'], help='El mensaje base a enviar.')

    return parser.parse_args()


def establish_connection():
    """
    Establece una conexión con RabbitMQ.
    Retorna el objeto de conexión si es exitoso.
    Salida del programa si hay un error de conexión.
    """

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        return connection

    except pika.exceptions.AMQPConnectionError as e:
        logging.error('\n[!] Error al conectar con RabbitMQ: %s', e)
        sys.exit(1)


def declare_exchange(channel):
    """
    Declara el intercambio de tipo 'topic'.
    Salida del programa si hay un error al declarar el intercambio.
    """

    try:
        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    except pika.exceptions.ChannelError as e:
        logging.error('\n[!] Error al declarar el intercambio: %s', e)
        sys.exit(1)


def generate_message(base_message):
    """
    Genera un mensaje único que incluye un número aleatorio, fecha y hora actual.
    """

    random_id = random.randint(
        1000, 9999)  # Genera un ID aleatorio de 4 dígitos
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Fecha y hora actual

    return f"{timestamp} - ({random_id}): {base_message}"


def publish_message(channel, routing_key, message):
    """
    Publica un mensaje en el intercambio declarado.
    """

    channel.basic_publish(exchange='topic_logs',
                          routing_key=routing_key, body=message)
    logging.info(' [+] Enviado %s:%s', routing_key, message)


def main():
    """
    Función principal que orquesta la ejecución del script.
    """

    # Parsear los argumentos de línea de comandos
    args = parse_arguments()
    routing_key = args.routing_key
    base_message = ' '.join(args.message)

    # Establecer conexión y publicar mensaje cada 5 segundos
    with establish_connection() as connection:
        channel = connection.channel()
        declare_exchange(channel)

        try:
            while True:
                # Generar y publicar el mensaje
                message = generate_message(base_message)
                publish_message(channel, routing_key, message)
                # Espera de 5 segundos antes de enviar el siguiente mensaje
                time.sleep(5)
        except KeyboardInterrupt:
            logging.info("\n[!] Interrupción del usuario. Terminando...")
        except Exception as e:
            logging.error("\n[!] Se produjo un error inesperado: %s", e)


if __name__ == '__main__':

    main()
