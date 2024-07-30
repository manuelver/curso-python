#!/usr/bin/env python
import pika
import sys
import os


def main():
    # Establecer la conexión con el servidor RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Asegurarnos de que la cola existe
    try:
        channel.queue_declare(queue='hola')
    except pika.exceptions.ChannelClosedByBroker:
        print(' [!] Error al crear la cola. ¿Está el servidor RabbitMQ corriendo?')
        sys.exit(1)
    except e:
        print(f' [!] Error: {e}')
        sys.exit(1)


    # Recibir mensajes de la cola es un poco más complejo que enviarlos.
    # Funciona suscribiendo una función callback a una cola.
    # Cada vez que recibimos un mensaje, esta función callback es llamada por la
    # librería Pika.
    # En nuestro caso esta función imprimirá en pantalla el contenido del mensaje.
    def callback(ch, method, properties, body):
        print(f" [+] Recibido \"{body.decode()}\"")

    # Ahora indicamos a RabbitMQ que comience a consumir mensajes de la cola.
    channel.basic_consume(
        queue='hola', auto_ack=True, on_message_callback=callback
    )

    # Bucle infinito que espera mensajes de la cola y llama a la función callback
    print(' [i] Esperando mensajes. Para salir presiona CTRL+C')
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
