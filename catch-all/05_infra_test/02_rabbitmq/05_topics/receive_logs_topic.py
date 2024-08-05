#!/usr/bin/env python
import pika
import argparse
import logging
import sys

# Configuración del logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def parse_arguments():
    """
    Analiza los argumentos de línea de comandos utilizando argparse.
    Devuelve un objeto con los argumentos proporcionados por el usuario.
    """

    parser = argparse.ArgumentParser(
        description='Recibe mensajes de un intercambio de tipo "topic" en RabbitMQ.')
    parser.add_argument('binding_keys', nargs='+',
                        help='Lista de claves de enlace para filtrar los mensajes.')

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
        logging.error('[!] Error al conectar con RabbitMQ: %s', e)
        sys.exit(1)


def declare_exchange_and_queue(channel):
    """
    Declara el intercambio de tipo 'topic' y una cola exclusiva.
    Retorna el nombre de la cola creada.
    """

    try:
        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        result = channel.queue_declare('', exclusive=True)

        return result.method.queue

    except pika.exceptions.ChannelError as e:
        logging.error('[!] Error al declarar el intercambio o la cola: %s', e)
        sys.exit(1)


def bind_queue(channel, queue_name, binding_keys):
    """
    Vincula la cola al intercambio con las claves de enlace proporcionadas.
    """

    for binding_key in binding_keys:
        try:
            channel.queue_bind(exchange='topic_logs',
                               queue=queue_name, routing_key=binding_key)
            logging.info(
                ' [i] Cola vinculada con clave de enlace: %s', binding_key)

        except pika.exceptions.ChannelError as e:
            logging.error(
                '[!] Error al vincular la cola con la clave de enlace %s: %s', binding_key, e)
            sys.exit(1)


def callback(ch, method, properties, body):
    """
    Función de callback que maneja los mensajes recibidos.
    """

    logging.info(' [+] %s: %s', method.routing_key.upper(), body.decode())


def start_consuming(channel, queue_name):
    """
    Inicia la recepción de mensajes desde la cola especificada.
    """

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    logging.info(' [i] Esperando mensajes. Para salir presione CTRL+C')

    try:
        channel.start_consuming()

    except KeyboardInterrupt:
        logging.info(' [!] Interrupción del usuario. Terminando...')
        channel.stop_consuming()


def main():
    """
    Función principal que orquesta la ejecución del script.
    """

    # Parsear los argumentos de línea de comandos
    args = parse_arguments()
    binding_keys = args.binding_keys

    # Establecer conexión, declarar intercambio y cola, vincular y comenzar a consumir
    with establish_connection() as connection:
        channel = connection.channel()
        queue_name = declare_exchange_and_queue(channel)
        bind_queue(channel, queue_name, binding_keys)
        start_consuming(channel, queue_name)


if __name__ == '__main__':

    main()
