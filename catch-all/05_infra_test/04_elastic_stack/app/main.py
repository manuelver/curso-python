import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Configura la conexión a Elasticsearch
es = Elasticsearch("http://elasticsearch:9200")


def create_index():
    """
    Crea un índice en Elasticsearch con el nombre 'movies' si no existe.
    Define el mapeo del índice para los campos de los documentos.
    """

    # Define el mapeo del índice 'movies'
    mappings = {
        "properties": {
            # Campo para el título de la película
            "title": {"type": "text", "analyzer": "english"},
            # Campo para la etnicidad
            "ethnicity": {"type": "text", "analyzer": "standard"},
            # Campo para el director
            "director": {"type": "text", "analyzer": "standard"},
            # Campo para el elenco
            "cast": {"type": "text", "analyzer": "standard"},
            # Campo para el género
            "genre": {"type": "text", "analyzer": "standard"},
            # Campo para el argumento de la película
            "plot": {"type": "text", "analyzer": "english"},
            # Campo para el año de lanzamiento
            "year": {"type": "integer"},
            # Campo para la página de Wikipedia
            "wiki_page": {"type": "keyword"}
        }
    }

    # Verifica si el índice 'movies' ya existe
    if not es.indices.exists(index="movies"):

        # Crea el índice 'movies' si no existe
        es.indices.create(index="movies", mappings=mappings)
        print("\n[+] Índice 'movies' creado.")

    else:

        print("\n[!] El índice 'movies' ya existe.")


def load_data():
    """
    Carga datos desde un archivo CSV a Elasticsearch.
    """

    try:

        # Lee el archivo CSV
        df = pd.read_csv("/app/wiki_movie_plots_deduped.csv", quoting=1)

        # Verifica el número de filas en el DataFrame
        num_rows = len(df)
        sample_size = min(5000, num_rows)

        # Elimina filas con valores nulos y toma una muestra
        df = df.dropna().sample(sample_size, random_state=42).reset_index(drop=True)

    except Exception as e:

        print(f"\n[!] Error al leer el archivo CSV: {e}")

        return

    # Prepara los datos para la carga en Elasticsearch
    bulk_data = [
        {
            "_index": "movies",  # Nombre del índice en Elasticsearch
            "_id": i,  # ID del documento en Elasticsearch
            "_source": {
                "title": row["Title"],  # Título de la película
                "ethnicity": row["Origin/Ethnicity"],  # Etnicidad
                "director": row["Director"],  # Director
                "cast": row["Cast"],  # Elenco
                "genre": row["Genre"],  # Género
                "plot": row["Plot"],  # Argumento
                "year": row["Release Year"],  # Año de lanzamiento
                "wiki_page": row["Wiki Page"],  # Página de Wikipedia
            }
        }
        for i, row in df.iterrows()  # Itera sobre cada fila del DataFrame
    ]

    try:

        # Carga los datos en Elasticsearch en bloques
        bulk(es, bulk_data)
        print("\n[+] Datos cargados en Elasticsearch.")

    except Exception as e:

        print(f"\n[!] Error al cargar datos en Elasticsearch: {e}")


def main():
    """
    Función principal que crea el índice y carga los datos.
    """

    create_index()  # Crea el índice en Elasticsearch
    load_data()  # Carga los datos en Elasticsearch


if __name__ == "__main__":
    # Ejecuta la función principal si el script se ejecuta directamente

    main()
