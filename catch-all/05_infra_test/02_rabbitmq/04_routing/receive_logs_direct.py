#!/usr/bin/env python
import pika
import sys
import argparse
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


def declare_exchange_and_queue(channel, exchange_name: str, severities: list):
    """Declara el intercambio y las colas necesarias."""

    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

    # Crear una cola exclusiva
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Vincular la cola al intercambio para cada severidad especificada
    for severity in severities:
        channel.queue_bind(
            exchange=exchange_name, queue=queue_name, routing_key=severity)

    return queue_name


def callback(ch, method, properties, body):
    """Función de callback para procesar mensajes recibidos."""

    print(f" [i] {method.routing_key}:{body.decode()}")


def main():

    parser = argparse.ArgumentParser(
        description='Recibe mensajes de RabbitMQ usando un intercambio directo.')
    parser.add_argument('--host', type=str, default='localhost',
                        help='El host de RabbitMQ (por defecto: localhost)')
    parser.add_argument('--port', type=int, default=5672,
                        help='El puerto de RabbitMQ (por defecto: 5672)')
    parser.add_argument('severities', metavar='S', type=str, nargs='+',
                        help='Lista de severidades a recibir (info, warning, error)')

    args = parser.parse_args()

    # Establecer conexión
    connection = establish_connection(args.host, args.port)
    channel = connection.channel()

    # Declarar el intercambio y las colas
    exchange_name = 'direct_logs'
    queue_name = declare_exchange_and_queue(
        channel, exchange_name, args.severities)

    print('\n[!] Esperando logs. Para salir presionar CTRL+C')

    # Iniciar el consumo de mensajes
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    # Manejar Ctrl+C para detener el programa
    try:
        channel.start_consuming()

    except KeyboardInterrupt:
        print("\nInterrupción recibida. Cerrando conexión...")
        connection.close()
        print("\n[!] Conexión cerrada. Programa terminado.")


if __name__ == '__main__':

    main()
