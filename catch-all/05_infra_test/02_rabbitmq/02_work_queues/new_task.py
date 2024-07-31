#!/usr/bin/env python
import pika
import sys


# Establecer la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Crear una cola llamada 'hola'
channel.queue_declare(queue='task_queue', durable=True)

# Mensaje a enviar
message = ' '.join(sys.argv[1:]) or "¡Hola mundo!"

# Enviar mensaje
channel.basic_publish(
    exchange='', routing_key='task_queue', body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    )
)

# Traza del envío
print(f" [+] Enviado '{message}'")

# Cerrar la conexión
connection.close()
