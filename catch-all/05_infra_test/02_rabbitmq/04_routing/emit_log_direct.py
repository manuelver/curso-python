#!/usr/bin/env python
import pika
import sys
import argparse
import time
import random
import datetime
import threading
import signal


def establish_connection(host: str, port: int):
    """Establece la conexión con RabbitMQ."""

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port)
        )

        return connection

    except pika.exceptions.AMQPConnectionError as e:
        print(f"\n[!] Error al conectar con RabbitMQ: {e}")
        sys.exit(1)


def publish_message(channel, exchange: str, severity: str, message: str):
    """Publica un mensaje en el intercambio especificado."""

    try:
        channel.basic_publish(
            exchange=exchange,
            routing_key=severity,
            body=message
        )
        print(f"[i] Sent {severity}:{message}")

    except Exception as e:
        print(f"\n[!] Error al enviar mensaje: {e}")
        sys.exit(1)


def send_messages_periodically(channel, exchange_name, severity, base_message):
    """Envía mensajes periódicamente cada 5 segundos hasta que se detenga."""

    try:
        while not stop_event.is_set():
            # Generar número aleatorio para identificar el envío
            random_number = random.randint(1000, 9999)

            # Obtener la fecha y hora actual
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Crear el mensaje con la fecha, hora y número aleatorio
            message = f"{base_message} [{random_number}] at {current_time}"

            # Publicar el mensaje
            publish_message(channel, exchange_name, severity, message)

            # Esperar 5 segundos antes de enviar el siguiente mensaje
            # Comprobación del evento de parada durante la espera
            for _ in range(50):
                if stop_event.is_set():
                    break

                time.sleep(0.1)

    except KeyboardInterrupt:
        stop_event.set()


def user_input_thread():
    """Hilo para capturar la entrada del usuario."""

    while not stop_event.is_set():
        user_input = input()
        if user_input.strip().lower() == 'q':
            stop_event.set()


def signal_handler(sig, frame):
    """Manejador de señal para terminar el programa."""

    stop_event.set()


def main():

    parser = argparse.ArgumentParser(
        description='Envía mensajes a RabbitMQ usando un intercambio directo.')
    parser.add_argument('--host', type=str, default='localhost',
                        help='El host de RabbitMQ (por defecto: localhost)')
    parser.add_argument('--port', type=int, default=5672,
                        help='El puerto de RabbitMQ (por defecto: 5672)')
    parser.add_argument('severity', type=str, nargs='?',
                        default='info', help='La severidad del mensaje')
    parser.add_argument('message', type=str, nargs='*',
                        default=['Hello', 'World!'], help='El mensaje a enviar')

    args = parser.parse_args()

    # Establecer conexión
    connection = establish_connection(args.host, args.port)
    channel = connection.channel()

    # Declarar intercambio
    exchange_name = 'direct_logs'
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

    # Mensaje base
    base_message = ' '.join(args.message)

    # Crear un hilo para el envío periódico de mensajes
    send_thread = threading.Thread(target=send_messages_periodically, args=(
        channel, exchange_name, args.severity, base_message))
    send_thread.start()

    # Crear un hilo para capturar la entrada del usuario
    input_thread = threading.Thread(target=user_input_thread)
    input_thread.start()

    print("Presiona 'q' para detener el envío de mensajes.")

    # Esperar a que los hilos terminen antes de cerrar la conexión
    send_thread.join()
    input_thread.join()

    # Cerrar conexión
    connection.close()
    print("Conexión cerrada. Programa terminado.")


if __name__ == '__main__':

    # Crear un evento para detener el envío de mensajes
    stop_event = threading.Event()

    # Configurar el manejador de señales para terminar el programa
    signal.signal(signal.SIGINT, signal_handler)

    main()
