#!/usr/bin/env python
import pika
import sys
import os
import time


def main():
    # Establecer la conexión con el servidor RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Comprobar si la cola existe
    try:
        channel.queue_declare(queue='task_queue', durable=True)
    except pika.exceptions.ChannelClosedByBroker:
        print(' [!] Error al crear la cola. ¿Está el servidor RabbitMQ corriendo?')
        sys.exit(1)
    except e:
        print(f' [!] Error: {e}')
        sys.exit(1)


    # Consumir mensajes

    def callback(ch, method, properties, body):
        print(f"[+] Recibido {body.decode()}")
        time.sleep(body.count(b'.'))
        print("[i] Hecho")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Consumir mensajes de la cola 'task_queue'
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    # Iniciar la escucha
    print('[i] Esperando mensajes. Para salir presiona CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' [!] Saliendo')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
