
# Configuración de Grafana con Prometheus para proyectos Python usando Docker

En este artículo, cubriremos cómo configurar el monitoreo de servicios para proyectos Python con Prometheus y Grafana utilizando contenedores Docker.

El monitoreo de servicios nos permite analizar eventos específicos en nuestros proyectos, tales como llamadas a bases de datos, interacción con API, seguimiento del rendimiento de recursos, etc. Puedes detectar fácilmente comportamientos inusuales o descubrir pistas útiles detrás de los problemas.

## Escenario de Caso Real

Teníamos un servicio temporal que redirigía las solicitudes entrantes de sitios web específicos hasta que Google dejara de indexar estas páginas web. Utilizando el monitoreo de servicios, podemos ver fácilmente el conteo de redirecciones de forma regular. En un momento determinado en el futuro, el número de redirecciones disminuirá, lo que significa que el tráfico se ha migrado al sitio web objetivo, y ya no necesitaremos que este servicio esté en funcionamiento.

## Configuración de contenedores Docker

Vamos a ejecutar todos nuestros servicios localmente en contenedores Docker. En las grandes empresas, existe un servicio global para Prometheus y Grafana que incluye todos los proyectos de monitoreo de microservicios. Probablemente ni siquiera necesites escribir ningún pipeline de despliegue para las herramientas de monitoreo de servicios.

### Archivo docker-compose.yml

Comencemos creando un archivo `docker-compose.yml` con los servicios necesarios:

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ${PWD}/prometheus.yml:/etc/prometheus/prometheus.yml
    restart: unless-stopped
    networks:
      - monitoring-net
    healthcheck:
      test: ["CMD", "wget", "--spider", "http://localhost:9090/-/healthy"]
      interval: 1m30s
      timeout: 30s
      retries: 3
      start_period: 30s

  grafana:
    hostname: grafana
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - 3001:3000
    restart: unless-stopped
    networks:
      - monitoring-net
    healthcheck:
      test: ["CMD", "wget", "--spider", "http://localhost:3000/api/health"]
      interval: 1m30s
      timeout: 30s
      retries: 3
      start_period: 30s

  app:
    build:
      context: .
      dockerfile: Dockerfile
    depends_on:
      - prometheus
    ports:
      - "8080:8080"
    networks:
      - monitoring-net
    command: ["python3", "app/main.py"]

networks:
  monitoring-net:
    driver: bridge
```

El punto más importante de la configuración anterior es montar el archivo `prometheus.yml` desde nuestra máquina local al contenedor Docker. Este archivo incluye la configuración para obtener datos (métricas) de nuestro servicio de aplicación o proyecto Python. Sin el archivo, no podrás ver las métricas personalizadas que incluye tu proyecto.

Por lo tanto, crea un nuevo archivo llamado `prometheus.yml` en el nivel raíz de tu proyecto.

### Archivo prometheus.yml

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'app'
    static_configs:
      - targets: ['app:8080']
```

Ahora, Prometheus obtendrá datos de nuestro proyecto.

Todas las demás configuraciones en el archivo de composición son autoexplicativas y no son muy críticas, como mencionamos para Prometheus.

## Crear un nuevo proyecto Python

Ahora, vamos a crear una aplicación Python muy sencilla que creará una métrica para rastrear el tiempo empleado y las solicitudes realizadas. Crea una nueva carpeta llamada `app` en el nivel raíz del proyecto. También incluye `__init__.py` para marcarla como un paquete Python.

A continuación, crea otro archivo llamado `main.py` que contendrá la lógica principal del programa, como se muestra a continuación:

### Archivo app/main.py

```python
from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
import random
import time

# Create metrics to track time spent, requests made, and other events.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
UPDATE_COUNT = Counter('update_count', 'Number of updates')
ACTIVE_REQUESTS = Gauge('active_requests', 'Number of active requests')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency in seconds')

# Decorate function with metrics.
@REQUEST_TIME.time()
@REQUEST_LATENCY.time()
def process_request(t):
    """A dummy function that takes some time."""
    ACTIVE_REQUESTS.inc()
    time.sleep(t)
    ACTIVE_REQUESTS.dec()

def main():
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("[*] Starting server on port 8000...")
    
    # Generate some requests.
    while True:
        msg = random.random()
        process_request(msg)
        update_increment = random.randint(1, 100)
        UPDATE_COUNT.inc(update_increment)
        print(f'[+] Processing request: {msg:.4f} | Updates: {update_increment}')
        time.sleep(random.uniform(0.5, 2.0))  # Random delay between requests

if __name__ == '__main__':
    main()
```

Aquí, estamos utilizando un paquete de Python llamado `prometheus_client` para interactuar con Prometheus. Permite fácilmente la creación de diferentes tipos de métricas que nuestro proyecto requiere.

El código anterior se copió de la documentación oficial de `prometheus_client`, que simplemente crea una nueva métrica llamada `request_processing_seconds` que mide el tiempo empleado en esa solicitud en particular. Cubriremos otros tipos de métricas más adelante en este artículo.

Ahora, vamos a crear un `Dockerfile` y un `requirements.txt` para construir nuestro proyecto.

### Archivo Dockerfile

```dockerfile
# Usa la imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY app/ /app

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "main.py"]
```

### Archivo requirements.txt

```txt
prometheus_client
```

Ahora estamos listos para construir y ejecutar los servicios.

## Ejecución de los servicios

Para ver todo en acción, ejecuta los siguientes comandos:

```bash
docker-compose up -d --build
```

Esto levantará todos los servicios definidos en `docker-compose.yml`, compilando la imagen de la aplicación en el proceso.

## Configuración de Grafana

En esta sección, usaremos Prometheus como fuente de datos para mostrar métricas en gráficos de Grafana.

1. Navega a `http://localhost:3001` para ver la página de inicio de sesión de Grafana y utiliza `admin` tanto para el nombre de usuario como para la contraseña. Luego, requerirá agregar una nueva contraseña, y puedes mantenerla igual ya que estamos probando localmente.

2. Después de iniciar sesión correctamente, deberías ver el panel predeterminado de Grafana. Luego selecciona **Data Sources** en la página.

   ![](https://res.cloudinary.com/practicaldev/image/fetch/s--dckjv7Wt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://www.thepylot.dev/content/images/size/w1000/2022/06/Screen-Shot-2022-06-11-at-16.51.10.png)

3. A continuación, selecciona Prometheus como fuente de datos:

   ![](https://res.cloudinary.com/practicaldev/image/fetch/s--v5aNeycU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://www.thepylot.dev/content/images/size/w1000/2022/06/Screen-Shot-2022-06-11-at-16.53.47.png)

4. Luego requerirá la URL en la que se está ejecutando el servicio de Prometheus, que será el nombre del servicio de Docker que creamos `http://prometheus:9090`.

   ![](https://res.cloudinary.com/practicaldev/image/fetch/s--cSw8NHIy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://www.thepylot.dev/content/images/size/w1000/2022/06/Screen-Shot-2022-06-11-at-16.56.09.png)

5. Finalmente, haz clic en el botón **Save & Test** para verificar la conexión de la fuente de datos.

   ![](https://res.cloudinary.com/practicaldev/image/fetch/s--i4CVmg76--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%

2Cw_800/https://www.thepylot.dev/content/images/size/w1000/2022/06/Screen-Shot-2022-06-11-at-16.56.55.png)

¡Genial! Ahora nuestro Grafana está listo para ilustrar las métricas que provienen de Prometheus.

## Creación de un nuevo dashboard en Grafana

1. Navega a `http://localhost:3001/dashboards` para crear un nuevo dashboard y agregar un nuevo panel. Haz clic en **New Dashboard** y luego en **Add New Panel** para la inicialización.

   ![](https://res.cloudinary.com/practicaldev/image/fetch/s--yZiKAdWz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://www.thepylot.dev/content/images/size/w1000/2022/06/Screen-Shot-2022-06-11-at-17.02.21.png)

2. A continuación, seleccionamos código dentro del panel de consultas y escribimos `request_processing_seconds`. Podrás ver 3 tipos diferentes de sufijos con los datos de tus métricas personalizadas. Prometheus simplemente aplica diferentes tipos de cálculos a tus datos de manera predeterminada.

3. Selecciona una de las opciones y haz clic en **Run Query** para verla en el gráfico.

   ![](https://res.cloudinary.com/practicaldev/image/fetch/s--E8k1_d3s--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://www.thepylot.dev/content/images/size/w1000/2022/06/Screen-Shot-2022-06-11-at-17.14.32.png)

Finalmente, podemos ver las métricas de nuestro proyecto ilustradas muy bien por Grafana.

## Otras métricas

Hay muchos tipos de métricas disponibles según lo que requiera el proyecto. Si queremos contar un evento específico, como actualizaciones de registros en la base de datos, podemos usar `Counter()`.

Si tenemos una cola de mensajes como Kafka o RabbitMQ, podemos usar `Gauge()` para ilustrar el número de elementos que esperan en la cola.

Intenta agregar otra métrica en `main.py` como se muestra a continuación y aplica los mismos pasos para conectar Prometheus con Grafana:

### Ejemplo de una nueva métrica con Counter

```python
UPDATE_COUNT = Counter('update_count', 'Number of updates')

# Dentro de tu función de procesamiento
update_increment = random.randint(1, 100)
UPDATE_COUNT.inc(update_increment)
```

No olvides construir nuevamente la imagen de Docker para todos los servicios:

```bash
docker-compose up -d --build
```

---
