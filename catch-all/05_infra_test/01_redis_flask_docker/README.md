# Crear una API Caching con Redis, Flask y Docker

<!-- Artículo original: https://dev.to/vjanz/implement-api-caching-with-redis-flask-and-docker-step-by-step-5h01 -->

![](https://res.cloudinary.com/practicaldev/image/fetch/s--MflWnlWv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://cdn-images-1.medium.com/max/4350/1%2AgEpkD_3NMTxK-w96c_QBBA.png)

## Prueba 1: Sin Redis

Primero vamos a hacer una prueba de la aplicación sin redis.

Vamos al directorio donde queremos trabajar, creamos un entorno virtual y lo activamos:

```bash
python3 -m venv venv
source venv/bin/activate
```

Ahora instalamos las dependencias en nuestro entorno:

```bash
(venv) pip install Flask redis flask_caching requests
```

Y guardamos estas dependencias en un archivo `requirements.txt`:

```bash
(venv) pip freeze > requirements.txt
```
Vamos a crear un archivo `app.py` con el siguiente contenido:

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/universities")
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

Ahora vamos a ejecutar la aplicación:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Y si nos vamos a postman podremos comprobar cuanto tarda en responder la petición:

![](https://res.cloudinary.com/practicaldev/image/fetch/s--cFeIXNRd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://cdn-images-1.medium.com/max/2898/1%2A9o8_94EDMwGO-BWWKnshBA.png)


## Prueba 2: Dockerizar nuestra aplicación

Vamos a dockerizar nuestra aplicación, para ello vamos a crear un archivo `Dockerfile` con el siguiente contenido:

```Dockerfile
FROM python:3.12-alpine AS builder

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
```

Vamos a crear también un archivo `docker-compose.yaml` con el siguiente contenido:

```yaml
version: '3.8'

services:
  api:
    container_name: app-python-flask-with-redis
    build: .
    env_file:
      - .env
    ports:
      - '5000:5000'
    depends_on:
      - redis

  redis:
    image: redis:7.0-alpine
    container_name: redis-python
    ports:
      - '6379:6379'
```

Incluimos también el contenedor de Redis. Lanzamos nuestra aplicación con el comando:

```bash
docker-compose up -d --build
```

Si vemos `docker ps` veremos que tenemos dos contenedores corriendo. También podemos revisar los logs del contenedor de la aplicación con `docker logs app-python-flask-with-redis`.

Comprobamos que nuestra aplicación sigue funcionando en docker igual que lo hacía en local.

## Prueba 3: Añadir Redis a nuestra aplicación

Ahora vamos a añadir Redis a nuestra aplicación. Vamos a modificar el archivo `app.py` para que use Redis:

```python
import requests
from flask import Flask, jsonify, request
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
cache = Cache(app)

@app.route("/universities")
@cache.cached(timeout=30, query_string=True)
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```


Y vamos a crear un archivo `config.py` con el siguiente contenido:

```python
import os

class BaseConfig(object):
    CACHE_TYPE = os.environ['CACHE_TYPE']
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
    CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']
```

Este fichero recoge las variables de entorno que vamos a usar en nuestra aplicación. Vamos a crear un archivo `.env` con el siguiente contenido:

```bash
# .e
CACHE_TYPE=redis
CACHE_REDIS_HOST=redis
CACHE_REDIS_PORT=6379
CACHE_REDIS_DB=0
CACHE_REDIS_URL=redis://redis:6379/0
CACHE_DEFAULT_TIMEOUT=300
```

Al finalizar la práctica, tendremos esta estructura:

```
.
├── app.py
├── config.py
├── docker-compose.yaml
├── Dockerfile
├── .env
└── requirements.txt
```

Volvemos a lanzar nuestra aplicación con `docker-compose up -d --build` y comprobamos que todo sigue funcionando correctamente. 

Volvemos a lanzar la misma petición desde postman y comprobamos que la respuesta es mucho más rápida que antes:

![](https://res.cloudinary.com/practicaldev/image/fetch/s--mHDsWyzq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://cdn-images-1.medium.com/max/2922/1%2Au4a8OUBQu2gBzvc6iL5nsw.png)


Podemos probar con otros países, la primera vez tardará más porque no estará en caché, pero las siguientes veces será mucho más rápido.

Esta es la magia de Redis, una base de datos en memoria que nos permite almacenar datos en caché y acelerar nuestras aplicaciones 🚀

