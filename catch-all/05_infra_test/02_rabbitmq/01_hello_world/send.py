#!/usr/bin/env python
import pika

# Establecer la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Crear una cola llamada 'hola'
channel.queue_declare(queue='hola')

# Enviar mensaje
channel.basic_publish(
    exchange='', routing_key='hola', body='¡Hola Mundo!'
)

# Traza del envío
print(" [+] Enviado 'Hola Mundo!'")

# Cerrar la conexión
connection.close()
