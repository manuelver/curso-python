#!/usr/bin/env python
import pika
from functools import lru_cache
import time

# Establecemos la conexión a RabbitMQ


def create_connection():

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )

        return connection

    except pika.exceptions.AMQPConnectionError as e:
        print(f"[!] Error al conectar a RabbitMQ: {e}")

        return None


# Conexión a RabbitMQ
connection = create_connection()

if not connection:
    exit(1)

# Canal de comunicación con RabbitMQ
channel = connection.channel()

# Declaración de la cola 'rpc_queue'
channel.queue_declare(queue='rpc_queue')

# Implementación mejorada de Fibonacci con memoización


@lru_cache(maxsize=None)
def fib(n):

    if n < 0:
        raise ValueError("\n[!] El número no puede ser negativo.")

    elif n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)

# Callback para procesar solicitudes RPC


def on_request(ch, method, props, body):

    try:
        n = int(body)
        print(f" [+] Calculando fib({n})")

        # Simula un tiempo de procesamiento de 2 segundos
        time.sleep(2)

        response = fib(n)
        print(f" [+] Resultado: {response}")

    except ValueError as e:
        response = f"\n[!] Error: {str(e)}"

    except Exception as e:
        response = f"\n[!] Error inesperado: {str(e)}"

    # Publicar la respuesta al cliente
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response)
    )

    # Confirmar la recepción del mensaje
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Configuración de calidad de servicio y consumo de mensajes
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print("\n[i] Esperando solicitudes RPC")
channel.start_consuming()
