import json
import logging
from time import sleep
from kafka import KafkaConsumer

# Configuración del registro
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():

    # Nombre del tema de Kafka del que se consumen los mensajes
    parsed_topic_name = 'parsed_recipes'

    # Umbral de calorías para la notificación
    calories_threshold = 200

    # Crear un consumidor de Kafka
    consumer = KafkaConsumer(
        parsed_topic_name,
        auto_offset_reset='earliest',  # Inicia desde el 1er mensaje si es nuevo
        bootstrap_servers=['kafka:9092'],  # Servidor Kafka
        api_version=(0, 10),  # Versión de la API de Kafka
        # Tiempo máx. de espera mensajes (milisegundos)
        consumer_timeout_ms=2000
    )

    logging.info('[+] Iniciando el consumidor de notificaciones...')

    try:

        for msg in consumer:

            # Decodificar el mensaje de JSON
            record = json.loads(msg.value)

            # Obtener el valor de calorías
            calories = int(record.get('calories', 0))
            title = record.get('title', 'Sin título')  # Obtener el título

            # Verificar si las calorías exceden el umbral
            if calories > calories_threshold:
                logging.warning(
                    f'[!] Alerta: {title} tiene {calories} calorías')

            # Esperar 5 segundos antes de procesar el siguiente mensaje
            sleep(5)

    except Exception as ex:

        logging.error(
            '[!] Error en el consumidor de notificaciones', exc_info=True)

    finally:

        if consumer is not None:
            consumer.close()  # Cerrar el consumidor al finalizar
            logging.info('[i] Consumidor cerrado.')


if __name__ == '__main__':

    main()
