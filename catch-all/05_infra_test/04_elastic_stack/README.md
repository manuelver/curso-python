
# Cómo Usar Elasticsearch en Python con Docker



**Índice**
- [Cómo Usar Elasticsearch en Python con Docker](#cómo-usar-elasticsearch-en-python-con-docker)
  - [¿Qué es Elasticsearch?](#qué-es-elasticsearch)
  - [Requisitos Previos](#requisitos-previos)
  - [Crear un Clúster Local del Elastic Stack con Docker Compose](#crear-un-clúster-local-del-elastic-stack-con-docker-compose)
    - [Desplegar el Elastic Stack](#desplegar-el-elastic-stack)
  - [Dockerizar el Programa Python](#dockerizar-el-programa-python)
    - [Programa Python](#programa-python)
  - [Conectar a Tu Clúster desde el Contenedor Python](#conectar-a-tu-clúster-desde-el-contenedor-python)
  - [Ejecutar los Scripts Python en Docker](#ejecutar-los-scripts-python-en-docker)
    - [Construir y Ejecutar el Contenedor Python](#construir-y-ejecutar-el-contenedor-python)
  - [Visualización de Datos con Kibana](#visualización-de-datos-con-kibana)
  - [Usar Logstash para Ingestión de Datos](#usar-logstash-para-ingestión-de-datos)
  - [Recopilar Métricas con Metricbeat](#recopilar-métricas-con-metricbeat)
  - [Eliminar Documentos del Índice](#eliminar-documentos-del-índice)
  - [Eliminar un Índice](#eliminar-un-índice)
  - [Conclusión](#conclusión)

[Elasticsearch](https://www.elastic.co/elasticsearch/) (ES) es una tecnología utilizada por muchas empresas, incluyendo GitHub, Uber y Facebook. Aunque no se enseña con frecuencia en cursos de Ciencia de Datos, es probable que te encuentres con ella en tu carrera profesional.

Muchos científicos de datos enfrentan dificultades al configurar un entorno local o al intentar interactuar con Elasticsearch en Python. Además, no hay muchos recursos actualizados disponibles.

Por eso, decidí crear este tutorial. Te enseñará lo básico y podrás configurar un clúster de Elasticsearch en tu máquina para el desarrollo local rápidamente. También aprenderás a crear un índice, almacenar datos en él y usarlo para buscar información.

¡Vamos a empezar!


## ¿Qué es Elasticsearch?

Elasticsearch es un motor de búsqueda distribuido, rápido y fácil de escalar, capaz de manejar datos textuales, numéricos, geoespaciales, estructurados y no estructurados. Es un motor de búsqueda popular para aplicaciones, sitios web y análisis de registros. También es un componente clave del Elastic Stack (también conocido como ELK Stack), que incluye Logstash y Kibana, junto con Beats para la recolección de datos.

Para entender el funcionamiento interno de Elasticsearch, piensa en él como dos procesos distintos. Uno es la ingestión, que normaliza y enriquece los datos brutos antes de indexarlos usando un [índice invertido](https://www.elastic.co/guide/en/elasticsearch/reference/current/documents-indices.html). El segundo es la recuperación, que permite a los usuarios recuperar datos escribiendo consultas que se ejecutan contra el índice.

Eso es todo lo que necesitas saber por ahora. A continuación, prepararás tu entorno local para ejecutar un clúster del Elastic Stack.

## Requisitos Previos

Debes configurar algunas cosas antes de comenzar. Asegúrate de tener lo siguiente listo:

1. Instala Docker y Docker Compose.
2. Descarga los datos necesarios.

## Crear un Clúster Local del Elastic Stack con Docker Compose

Para desplegar el Elastic Stack (Elasticsearch, Kibana, Logstash y Beats) en tu máquina local, utilizaremos Docker Compose. Este enfoque simplifica el despliegue y la administración de múltiples servicios.

Mediante el fichero [docker-compose.yaml](docker-compose.yaml) vamos a configurar los servicios para Elasticsearch, Kibana, Logstash, Metricbeat, y la aplicación Python, todos conectados a una red llamada `elastic`.


### Desplegar el Elastic Stack

Para iniciar los servicios, abre una terminal en el directorio donde se encuentra `docker-compose.yml` y ejecuta el siguiente comando:

```bash
docker compose up -d
```

Este comando iniciará Elasticsearch, Kibana, Logstash, Metricbeat y la aplicación Python en contenedores separados. Aquí tienes un desglose de los servicios:

- **Elasticsearch**: El motor de búsqueda que almacena y analiza los datos.
- **Kibana**: Una interfaz de usuario para visualizar y explorar datos en Elasticsearch.
- **Logstash**: Una herramienta de procesamiento de datos que ingiere datos desde múltiples fuentes, los transforma y los envía a un destino como Elasticsearch.
- **Metricbeat**: Un agente de monitoreo que recopila métricas del sistema y las envía a Elasticsearch.
- **Python App**: Un contenedor que ejecutará tus scripts de Python para interactuar con Elasticsearch. (Hasta que no construyamos el contenedor, este servicio fallará).


## Dockerizar el Programa Python

Para dockerizar la aplicación Python, utilizaremos el archivo [Dockerfile](./app/Dockerfile) del directorio `app`. El directorio `app` también debe contener el programa Python y un archivo [requirements.txt](./app/requirements.txt) para manejar las dependencias.

### Programa Python

El archivo [main.py](./app/main.py) en el directorio `app` manejará la conexión a Elasticsearch, la creación de índices y la carga de datos.

Este programa realiza las siguientes acciones:

1. **Crea un índice** en Elasticsearch con las configuraciones de mapeo necesarias.
2. **Carga datos** desde un archivo CSV (`wiki_movie_plots_deduped.csv`) al índice creado.


## Conectar a Tu Clúster desde el Contenedor Python

Tu aplicación Python se conectará al clúster de Elasticsearch usando el hostname `elasticsearch`, que es el nombre del servicio definido en `docker-compose.yml`.


## Ejecutar los Scripts Python en Docker

Una vez que hayas creado los archivos `Dockerfile`, `requirements.txt` y `main.py`, puedes construir la imagen de Docker para tu aplicación Python y ejecutarla usando Docker Compose.


### Construir y Ejecutar el Contenedor Python

1. Construye la imagen de Docker para tu aplicación Python:

    ```bash
    docker compose build python-app
    ```

2. Ejecuta el contenedor:

    ```bash
    docker compose up python-app
    ```

La aplicación Python se ejecutará y cargará los datos en Elasticsearch. Puedes verificar que los datos se hayan indexado correctamente ejecutando una consulta en Elasticsearch o usando Kibana para explorar los datos:
    
```python
es.search(index="movies", body={"query": {"match_all": {}}})
```


## Visualización de Datos con Kibana

Kibana es una herramienta de visualización que se conecta a Elasticsearch y te permite explorar y visualizar tus datos.

Para acceder a Kibana, abre un navegador web y navega a `http://localhost:5601`. Deberías ver la interfaz de Kibana, donde puedes crear visualizaciones y dashboards.

1. **Crea un índice en Kibana**: Ve a *Management > Index Patterns* y crea un nuevo patrón de índice para el índice `movies`.
2. **Explora tus datos**: Usa la herramienta *Discover* para buscar y explorar los datos que has indexado.
3. **Crea visualizaciones**: En la sección *Visualize*, crea gráficos y tablas que te permitan entender mejor tus datos.


## Usar Logstash para Ingestión de Datos

Logstash es una herramienta para procesar y transformar datos antes de enviarlos a Elasticsearch. Aquí tienes un ejemplo básico de cómo configurar Logstash para que procese y envíe datos a Elasticsearch.

Mediante el archivo de configuración en la carpeta `logstash-config/` llamado [pipeline.conf](./logstash-config/pipeline.conf) realizaremos los siguientes pasos:

- Lee un archivo CSV de entrada.
- Usa el filtro `csv` para descomponer cada línea en campos separados.
- Usa `mutate` para convertir el año de lanzamiento en un número entero.
- Envía los datos procesados a Elasticsearch.

Para usar Logstash con esta configuración, asegúrate de que el archivo `wiki_movie_plots_deduped.csv` esté accesible en tu sistema y modifica la ruta en el archivo de configuración según sea necesario. Luego, reinicia el contenedor de Logstash para aplicar los cambios.

```bash
docker compose restart logstash
```


## Recopilar Métricas con Metricbeat

Metricbeat es un agente ligero que recopila métricas del sistema y las envía a Elasticsearch. Está configurado en el archivo `docker-compose.yml` que has creado anteriormente.

Para ver las métricas en Kibana:

1. **Configura Metricbeat**: Edita el archivo de configuración de Metricbeat si necesitas recopilar métricas específicas.
2. **Importa dashboards preconfigurados**: En Kibana, navega a *Add Data > Metricbeat* y sigue las instrucciones para importar los dashboards preconfigurados.
3. **Explora las métricas**: Usa los dashboards importados para explorar las métricas de tu sistema.


## Eliminar Documentos del Índice

Puedes usar el siguiente código para eliminar documentos del índice:

```python
es.delete(index="movies", id="2500")
```

El código anterior eliminará el documento con ID 2500 del índice `movies`.


## Eliminar un Índice

Finalmente, si por alguna razón deseas eliminar un índice (y todos sus documentos), aquí te mostramos cómo hacerlo:

```python
es.indices.delete(index='movies')
```


## Conclusión

Este tutorial te enseñó los conceptos básicos de Elasticsearch y cómo usarlo junto con el Elastic Stack y Docker. Esto será útil en tu carrera, ya que seguramente te encontrarás con Elasticsearch en algún momento.

En este tutorial, has aprendido:

- Cómo configurar un clúster del Elastic Stack en tu máquina usando Docker Compose.
- Cómo dockerizar una aplicación Python para interactuar con Elasticsearch.
- Cómo crear un índice y almacenar datos en él.
- Cómo buscar tus datos usando Elasticsearch.
- Cómo visualizar datos con Kibana.
- Cómo procesar datos con Logstash.
- Cómo recopilar métricas con Metricbeat.

Explora más funcionalidades de Elasticsearch y el Elastic Stack para sacar el máximo provecho de tus datos.
