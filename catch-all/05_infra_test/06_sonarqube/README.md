
# SonarQube Python Analysis con Docker

Este tutorial te guía a través de la configuración y ejecución de un análisis de calidad de código de un proyecto Python utilizando SonarQube y Docker Compose.

## Requisitos previos

- Docker y Docker Compose instalados en tu máquina.

## Estructura del proyecto

Asegúrate de que tu directorio de proyecto tenga la siguiente estructura:

```
my-python-project/
│
├── app/                   
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
│
├── sonar-project.properties
├── docker-compose.yaml
└── README.md
```

## Paso 1: Crear un Proyecto Python de Ejemplo

Dentro de la carpeta `app`, crea los siguientes archivos:

### `main.py`

```python
def greet(name):
    return f"Hola, {name}!"

if __name__ == "__main__":
    print(greet("mundo"))
```

### `utils.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### `__init__.py`

Este archivo puede estar vacío, simplemente indica que `app` es un paquete Python.

## Paso 2: Configurar SonarQube y SonarScanner

### 2.1. Archivo `sonar-project.properties`

En la raíz de tu proyecto, crea un archivo llamado `sonar-project.properties` con el siguiente contenido:

```properties
sonar.projectKey=my-python-project
sonar.projectName=My Python Project
sonar.projectVersion=1.0
sonar.sources=./app
sonar.language=py
sonar.python.version=3.8
sonar.host.url=http://sonarqube:9000
sonar.login=admin
sonar.password=admin
```

Asegúrate de reemplazar `my-python-project`, `My Python Project`, y la ruta del código fuente según corresponda.

## Paso 3: Crear `docker-compose.yaml`

Crea un archivo `docker-compose.yaml` en la raíz de tu proyecto con el siguiente contenido:

```yaml
services:
  sonarqube:
    image: sonarqube:lts-community
    container_name: sonarqube
    ports:
      - "9001:9000"
    environment:
      - SONARQUBE_JDBC_URL=jdbc:postgresql://sonarqube-db:5432/sonar
      - SONARQUBE_JDBC_USERNAME=sonar
      - SONARQUBE_JDBC_PASSWORD=sonar
      - SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_extensions:/opt/sonarqube/extensions
    networks:
      - sonarnet
    depends_on:
      - elasticsearch
      - sonarqube-db

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.10.2
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data
    networks:
      - sonarnet

  sonarqube-db:
    image: postgres:16.3-alpine3.20
    container_name: sonarqube-db
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=sonar
      - POSTGRES_DB=sonar
    networks:
      - sonarnet
    volumes:
      - sonar_db:/var/lib/postgresql
      - sonar_db_data:/var/lib/postgresql/data

  sonarscanner:
    image: sonarsource/sonar-scanner-cli
    container_name: sonarscanner
    depends_on:
      - sonarqube
    volumes:
      - .:/usr/src
    working_dir: /usr/src
    networks:
      - sonarnet
    entrypoint: ["sonar-scanner"]

networks:
  sonarnet:
    driver: bridge

volumes:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_extensions:
  elasticsearch_data:
  sonar_db:
  sonar_db_data:
```

### Explicación

- **SonarQube**: Configurado para depender de Elasticsearch y PostgreSQL. Usa el contenedor `sonarqube:lts-community` que incluye SonarQube.
- **Elasticsearch**: Usa una imagen oficial de Elasticsearch (versión 7.10.2) adecuada para la versión de SonarQube que estás utilizando. Configurado para funcionar en modo de nodo único (`discovery.type=single-node`).
- **PostgreSQL**: Configurado para servir como la base de datos para SonarQube.
- **SonarScanner**: Configurado para ejecutar el análisis de código.

## Paso 4: Ejecutar el Análisis

1. **Inicia SonarQube, Elasticsearch y PostgreSQL**:

   En el directorio raíz de tu proyecto, ejecuta el siguiente comando para iniciar los servicios:

   ```bash
   docker-compose up -d
   ```

   Esto levantará los contenedores de SonarQube, Elasticsearch y PostgreSQL. Dale unos minutos para que se inicien completamente.

2. **Ejecuta el Análisis**:

   Una vez que SonarQube, Elasticsearch y PostgreSQL estén listos, ejecuta el siguiente comando para iniciar el análisis del código:

   ```bash
   docker-compose run sonarscanner
   ```

## Paso 5: Ver los Resultados

Accede a la interfaz de SonarQube en [http://localhost:9000](http://localhost:9000). Inicia sesión con las credenciales predeterminadas:

- Usuario: `admin`
- Contraseña: `admin`

Aquí podrás ver los resultados del análisis de calidad de tu código, incluyendo cualquier vulnerabilidad o deuda técnica identificada.

## Paso 6: Detener y Limpiar los Contenedores

Para detener y eliminar los contenedores, ejecuta:

```bash
docker-compose down
```

Esto detendrá los servicios y limpiará los recursos.

## Notas Finales

- Asegúrate de ajustar el archivo `sonar-project.properties` para que coincida con las especificaciones de tu proyecto.
- Puedes personalizar la configuración del contenedor de SonarQube en el archivo `docker-compose.yaml` según sea necesario.

¡Disfruta de un análisis de código más limpio y seguro con SonarQube!


