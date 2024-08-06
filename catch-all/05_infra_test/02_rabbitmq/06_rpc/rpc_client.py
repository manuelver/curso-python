#!/usr/bin/env python
import pika
import uuid
import sys
import argparse


class FibonacciRpcClient:
    def __init__(self, host='localhost'):
        # Establece la conexión con RabbitMQ
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=host)
            )
        except pika.exceptions.AMQPConnectionError as e:
            print(f"[!] Error al conectar con RabbitMQ: {e}")
            sys.exit(1)

        # Crea un canal de comunicación
        self.channel = self.connection.channel()

        # Declara una cola exclusiva para recibir las respuestas del servidor RPC
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        # Configura el canal para consumir mensajes de la cola de respuestas
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        # Inicializa las variables para manejar la respuesta RPC
        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        """Callback ejecutado al recibir una respuesta del servidor RPC."""
        # Verifica si el ID de correlación coincide con el esperado
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        """
        Envía una solicitud RPC para calcular el número de Fibonacci de n.

        :param n: Número entero no negativo para calcular su Fibonacci.
        :return: Resultado del cálculo de Fibonacci.
        :raises ValueError: Si n no es un número entero no negativo.
        """
        # Verifica que la entrada sea un número entero no negativo
        if not isinstance(n, int) or n < 0:
            raise ValueError("[!] El argumento debe ser un entero no negativo.")

        # Resetea la respuesta y genera un nuevo ID de correlación único
        self.response = None
        self.corr_id = str(uuid.uuid4())

        # Publica un mensaje en la cola 'rpc_queue' con las propiedades necesarias
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,  # Cola de retorno para recibir la respuesta
                correlation_id=self.corr_id,   # ID único para correlacionar la respuesta
            ),
            body=str(n)
        )

        # Espera hasta que se reciba la respuesta del servidor
        while self.response is None:
            self.connection.process_data_events(time_limit=None)

        # Devuelve la respuesta convertida a un entero
        return int(self.response)

    def close(self):
        """Cierra la conexión con el servidor de RabbitMQ."""
        self.connection.close()


if __name__ == "__main__":
    # Configura el analizador de argumentos para recibir el número de Fibonacci
    parser = argparse.ArgumentParser(
        description="Calcula números de Fibonacci mediante RPC.")
    parser.add_argument(
        "number",
        type=int,
        help="Número entero no negativo para calcular su Fibonacci."
    )
    args = parser.parse_args()

    # Inicializa el cliente RPC de Fibonacci
    fibonacci_rpc = FibonacciRpcClient()

    # Número para el cual se desea calcular el Fibonacci
    n = args.number

    try:
        print(f" [+] Solicitando fib({n})")
        # Realiza la llamada RPC y obtiene el resultado
        response = fibonacci_rpc.call(n)
        print(f" [+] Resultado fib({n}) = {response}")

    except ValueError as e:
        print(f"[!] Error de valor: {e}")

    except Exception as e:
        print(f"[!] Error inesperado: {e}")

    finally:
        # Cierra la conexión del cliente RPC
        fibonacci_rpc.close()
