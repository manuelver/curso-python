#!/usr/bin/env python
import argparse
import logging
import pika
import sys
import threading
import time
from datetime import datetime
from random import randint


def main():
    # Configuración de logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Configuración de argparse para manejar argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Envía un mensaje al intercambio de logs en RabbitMQ."
    )
    parser.add_argument(
        'message',
        nargs='*',
        help='El mensaje a enviar. Si no se especifica, se enviará "Traza de log"'
    )
    parser.add_argument(
        '--host', default='localhost',
        help='El host de RabbitMQ (default: localhost)'
    )
    parser.add_argument(
        '--user', default='invent',
        help='El usuario de RabbitMQ (default: invent)'
    )
    parser.add_argument(
        '--password', default='123456',
        help='La contraseña de RabbitMQ (default: 123456)'
    )
    args = parser.parse_args()

    # Crear el mensaje base
    base_message = ' '.join(args.message) or "Traza de log"

    stop_sending = threading.Event()

    def send_messages():
        credentials = pika.PlainCredentials(args.user, args.password)
        try:
            # Establecer conexión con RabbitMQ
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=args.host, credentials=credentials)
            )
            channel = connection.channel()

            # Declarar el intercambio de tipo 'fanout'
            channel.exchange_declare(exchange='logs', exchange_type='fanout')

            while not stop_sending.is_set():
                # Crear mensaje con fecha y hora actual
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                num_logs = randint(1, 1000)
                message = f"{current_time} - CUSTOM_LOG - {base_message}: Número aleatorio: {num_logs}"

                # Publicar el mensaje en el intercambio
                channel.basic_publish(
                    exchange='logs', routing_key='', body=message)
                logging.info(f"[+] Sent {message}")

                # Esperar 5 segundos antes de enviar el siguiente mensaje
                time.sleep(5)

        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"[!] No se pudo conectar a RabbitMQ: {e}")
        except Exception as e:
            logging.error(f"[!] Ocurrió un error: {e}")
        finally:
            # Cerrar la conexión
            if 'connection' in locals() and connection.is_open:
                connection.close()

    # Iniciar el hilo que enviará mensajes
    sender_thread = threading.Thread(target=send_messages)
    sender_thread.start()

    try:
        # Esperar a que el usuario introduzca 'q' para detener el envío de mensajes
        while True:
            user_input = input()
            if user_input.strip().lower() == 'q':
                stop_sending.set()
                sender_thread.join()
                break
    except KeyboardInterrupt:
        stop_sending.set()
        sender_thread.join()
        logging.info("Interrupción del usuario recibida. Saliendo...")


if __name__ == "__main__":
    main()
