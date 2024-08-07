import requests
from time import sleep
import logging
from bs4 import BeautifulSoup
from kafka import KafkaProducer


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
            topic_name, key=key_bytes, value=value_bytes
        )
        producer_instance.flush()  # Asegurar que el mensaje ha sido enviado
        logging.info('[+] Mensaje publicado con éxito.')

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


def fetch_raw(recipe_url):
    """
    Obtiene el HTML sin procesar de la URL de la receta.
    """

    html = None
    logging.info('[i] Procesando... {}'.format(recipe_url))

    try:

        r = requests.get(recipe_url, headers=headers)

        if r.status_code == 200:
            html = r.text

    except Exception as ex:

        logging.error(
            '[!] Error al acceder al HTML sin procesar',
            exc_info=True
        )

    return html.strip() if html else ''


def get_recipes():
    """
    Obtiene una lista de recetas de la URL de origen.
    """

    recipes = []
    url = 'https://www.allrecipes.com/recipes/96/salad/'

    logging.info('[i] Accediendo a la lista de recetas...')

    try:
        r = requests.get(url, headers=headers)
        logging.info('[i] Código de respuesta: {}'.format(r.status_code))

        if r.status_code == 200:
            logging.info('[i] Página accesible, procesando...')

            html = r.text
            soup = BeautifulSoup(html, 'lxml')

            # Selecciona los elementos <a> con la clase mntl-card-list-items
            links = soup.select('a.mntl-card-list-items')

            logging.info('[i] Se encontraron {} recetas'.format(len(links)))

            for link in links:
                # Obtiene el título del texto de card__title-text
                recipe_title = link.select_one(
                    '.card__title-text').get_text(strip=True)
                recipe_url = link['href']
                logging.info(
                    f'[i] Procesando receta: {recipe_title}, enlace: {recipe_url}'
                )

                sleep(2)
                recipe_html = fetch_raw(recipe_url)

                if recipe_html:
                    recipes.append(recipe_html)

            logging.info(
                '[i] Se obtuvieron {} recetas en total.'.format(len(recipes)))

        else:
            logging.error(
                '[!] No se pudo acceder a la página de recetas, código de respuesta: {}'.format(r.status_code))

    except Exception as ex:
        logging.error('[!] Error en get_recipes', exc_info=True)

    return recipes


def main():
    """
    Ejecuta el proceso de obtención y publicación de recetas.
    """

    global headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }

    logging.info('Iniciando el productor de recetas...')

    all_recipes = get_recipes()  # Obtener recetas

    if all_recipes:

        producer = connect_kafka_producer()  # Conectar con Kafka

        if producer:

            for recipe in all_recipes:

                publish_message(producer, 'raw_recipes', 'raw', recipe.strip())

            producer.close()  # Cerrar el productor

        else:

            logging.error('[!] El productor de Kafka no está disponible.')


if __name__ == '__main__':

    main()
