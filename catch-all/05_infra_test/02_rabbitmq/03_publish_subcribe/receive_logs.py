#!/usr/bin/env python
import pika
import logging
import argparse


def main():
    # Configuración de logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Configuración de argparse para manejar argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Escucha mensajes del intercambio de logs en RabbitMQ."
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

    credentials = pika.PlainCredentials(args.user, args.password)

    try:
        # Establecer conexión con RabbitMQ
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=args.host, credentials=credentials)
        )
        channel = connection.channel()

        # Declarar el intercambio de tipo 'fanout'
        channel.exchange_declare(exchange='logs', exchange_type='fanout')

        # Declarar una cola exclusiva para el consumidor
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        # Enlazar la cola al intercambio de logs
        channel.queue_bind(exchange='logs', queue=queue_name)

        logging.info(' [*] Waiting for logs. To exit press CTRL+C')

        # Función de callback para manejar mensajes entrantes
        def callback(ch, method, properties, body):
            logging.info(f" [x] Received: {body.decode()}")

        # Configurar el consumidor
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Iniciar el bucle de consumo
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        logging.error(f"[!] No se pudo conectar a RabbitMQ: {e}")
    except KeyboardInterrupt:
        logging.info("Interrupción del usuario recibida. Saliendo...")
    except Exception as e:
        logging.error(f"[!] Ocurrió un error: {e}")
    finally:
        # Cerrar la conexión si está abierta
        if 'connection' in locals() and connection.is_open:
            connection.close()


if __name__ == "__main__":
    main()
