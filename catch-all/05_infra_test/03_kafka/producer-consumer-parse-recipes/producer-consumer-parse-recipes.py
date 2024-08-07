import json
import logging
from time import sleep
from bs4 import BeautifulSoup
from kafka import KafkaConsumer, KafkaProducer

# Configuración del registro
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def publish_message(producer_instance, topic_name, key, value):
    """
    Publica un mensaje en el tema de Kafka especificado.
    """

    try:
        key_bytes = bytes(key, encoding='utf-8')  # Convertir clave a bytes
        value_bytes = bytes(value, encoding='utf-8')  # Convertir valor a bytes
        producer_instance.send(  # Enviar mensaje
            topic_name, key=key_bytes,
            value=value_bytes
        )
        producer_instance.flush()  # Asegurar que el mensaje ha sido enviado

        logging.info('[i] Mensaje publicado con éxito.')

    except Exception as ex:

        logging.error('[!] Error al publicar mensaje', exc_info=True)


def connect_kafka_producer():
    """
    Conecta y devuelve una instancia del productor de Kafka.
    """

    try:
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],  # Servidor Kafka
            api_version=(0, 10)  # Versión de la API de Kafka
        )

        logging.info('[i] Conectado con éxito al productor de Kafka.')

        return producer

    except Exception as ex:

        logging.error('[!] Error al conectar con Kafka', exc_info=True)

        return None


def parse(markup):
    """
    Analiza el HTML y extrae la información de la receta.
    """

    title = '-'
    submit_by = '-'
    description = '-'
    calories = 0
    ingredients = []
    rec = {}

    try:
        soup = BeautifulSoup(markup, 'lxml')  # Analizar HTML con BeautifulSoup

        # Actualizar selectores CSS para el título, descripción, ingredientes y calorías
        title_section = soup.select_one('h1.headline.heading-content')  # Título
        submitter_section = soup.select_one('span.author-name')  # Autor
        description_section = soup.select_one('div.recipe-summary > p')  # Descripción
        ingredients_section = soup.select('li.ingredients-item')  # Ingredientes
        calories_section = soup.select_one('span.calorie-count')  # Calorías

        # Extraer calorías
        if calories_section:
            calories = calories_section.get_text(strip=True).replace('cals', '').strip()

        # Extraer ingredientes
        if ingredients_section:
            for ingredient in ingredients_section:
                ingredient_text = ingredient.get_text(strip=True)
                if 'Add all ingredients to list' not in ingredient_text and ingredient_text != '':
                    ingredients.append({'step': ingredient_text})

        # Extraer descripción
        if description_section:
            description = description_section.get_text(strip=True)

        # Extraer nombre del autor
        if submitter_section:
            submit_by = submitter_section.get_text(strip=True)

        # Extraer título
        if title_section:
            title = title_section.get_text(strip=True)

        # Crear diccionario con la información de la receta
        rec = {
            'title': title,
            'submitter': submit_by,
            'description': description,
            'calories': calories,
            'ingredients': ingredients
        }

        logging.info(f"[i] Receta extraída: {rec}")

    except Exception as ex:

        logging.error('[!] Error en parsing', exc_info=True)

    return json.dumps(rec)


def main():
    """
    Ejecuta el proceso de consumo y publicación de mensajes.
    """

    topic_name = 'raw_recipes'
    parsed_topic_name = 'parsed_recipes'
    parsed_records = []

    # Crear un consumidor de Kafka
    consumer = KafkaConsumer(
        topic_name,
        auto_offset_reset='earliest',
        bootstrap_servers=['kafka:9092'],
        api_version=(0, 10),
        consumer_timeout_ms=2000
    )

    logging.info('[i] Iniciando el consumidor para parsing...')

    try:
        for msg in consumer:
            html = msg.value
            result = parse(html)  # Analizar el HTML
            parsed_records.append(result)

        consumer.close()  # Cerrar el consumidor

        logging.info('[i] Consumidor cerrado.')

        if parsed_records:
            logging.info('[+] Publicando registros...')
            producer = connect_kafka_producer()

            if producer:
                for rec in parsed_records:
                    publish_message(producer, parsed_topic_name, 'parsed', rec)

                producer.close()  # Cerrar el productor
            else:
                logging.error('[!] El productor de Kafka no está disponible.')

    except Exception as ex:
        logging.error('[!] Error en el productor-consumer', exc_info=True)


if __name__ == '__main__':
    main()
