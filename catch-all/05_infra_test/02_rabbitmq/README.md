# Pruebas con rabbitmq

*Índice de contenidos:*
- [Pruebas con rabbitmq](#pruebas-con-rabbitmq)
  - [Despliegue rabbitmq con docker](#despliegue-rabbitmq-con-docker)
  - [Pruebas](#pruebas)
    - [Hello World](#hello-world)
    - [Work Queues](#work-queues)
    - [Publish/Subscribe](#publishsubscribe)
    - [Routing](#routing)
      - [Enlaces](#enlaces)
      - [Intercambio Directo](#intercambio-directo)
      - [Múltiples Enlaces](#múltiples-enlaces)
      - [Emisión de Logs](#emisión-de-logs)
      - [Suscripción](#suscripción)
      - [Código de Ejemplo](#código-de-ejemplo)
      - [Ejemplos de Uso](#ejemplos-de-uso)
    - [Topics (Próximamente)](#topics-próximamente)
    - [RPC (Próximamente)](#rpc-próximamente)


## Despliegue rabbitmq con docker

Para desplegar RabbitMQ rápidamente, puedes usar Docker. Ejecuta el siguiente comando para iniciar un contenedor con RabbitMQ y su consola de gestión:

```bash
docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 -p 5672:5672 rabbitmq:3-management
```

Si prefieres usar docker-compose, utiliza el archivo [docker-compose.yaml](./docker-compose.yaml) con el siguiente comando:

```bash
docker compose up -d
```

## Pruebas

Pruebas extraídas de los tutoriales de la [documentación oficial de RabbitMQ](https://www.rabbitmq.com/tutorials#queue-tutorials).

### Hello World

Lo más sencillo que hace algo.

Tenemos que diferenciar algunos conceptos:
- **Producer**: es el que envía mensajes.
- **Queue**: es donde se almacenan los mensajes.
- **Consumer**: es el que recibe mensajes.

![](https://pica.zhimg.com/v2-35910cd84c7a62ad06cd4621b3d0523b_720w.jpg)

Vamos a programar un producer y un consumer en Python.

RabbitMQ habla múltiples protocolos. Este tutorial utiliza AMQP 0-9-1, que es un protocolo abierto de propósito general para mensajería. 

Hay un gran número de clientes para RabbitMQ en muchos idiomas diferentes. En esta serie de tutoriales vamos a usar Pika 1.0.0, que es el cliente Python recomendado por el equipo de RabbitMQ. Para instalarlo puedes usar la herramienta de gestión de paquetes pip:

```bash
pip install pika --upgrade
```

Nuestro primer programa [send.py](./hello-world/send.py) será el producer que enviará un único mensaje a la cola. Este script también crea la cola `hola`.

El programa [receive.py](./hello-world/receive.py) será el consumer que recibirá mensajes de la cola y los imprimirá en pantalla.

Desde la instalación de rabbitmq puedes ver qué colas tiene RabbitMQ y cuántos mensajes hay en ellas con rabbitmqctl:

```bash
sudo rabbitmqctl list_queues
```

Antes tendrás que entrar en el contenedor de rabbitmq:

```bash
docker exec -it rabbitmq-server bash
```

Ahora, para probarlo, ejecuta el producer y el consumer en dos terminales diferentes:

```bash
cd hello-world

python send.py

python receive.py
```

### Work Queues

Reparto de tareas entre los trabajadores (el modelo de consumidores competidores).

![](https://mail.bogotobogo.com/python/images/RabbitMQ_Celery/WorkQueues/WorkQueues.png)


Antes hemos enviado un mensaje que contenía `¡Hola Mundo!`. Ahora enviaremos cadenas que representan tareas complejas. No tenemos una tarea del mundo real, como imágenes para ser redimensionadas o archivos pdf para ser renderizados, así que vamos a fingir que estamos ocupados usando la función `time.sleep()`. Tomaremos el número de puntos de la cadena como su complejidad; cada punto representará un segundo de «trabajo». Por ejemplo, una tarea falsa descrita por Hola... tardará tres segundos.

Vamos a modificar el anterior send.py para permitir el envío de mensajes arbitrarios desde la línea de comando. Le llamaremos [new_task.py](./02work-queues/new_task.py).

También modificaremos receive.py para simular un segundo trabajao por cada punto en el cuerpo del mensaje. Como sacará mensajes de la cola y realizará la tarea le llamaremos [worker.py](./02work-queues/worker.py).


Ahora, si ejecutamos dos veces o más el script worker.py, veremos cómo se reparten las tareas entre los dos consumidores.

En dos terminales distintas:
```bash
cd 02work-queues

python worker.py
```

Y en la tercera terminal enviaremos trabajos:
```bash
python new_task.py Primer mensaje.
python new_task.py Segundo mensaje..
python new_task.py Tercer mensaje...
python new_task.py Cuarto mensaje....
python new_task.py Quinto mensaje.....
```

Por defecto, RabbitMQ enviará cada mensaje al siguiente consumidor, en secuencia. Por término medio, cada consumidor recibirá el mismo número de mensajes. Esta forma de distribuir mensajes se llama round-robin. 

Para asegurarse de que un mensaje nunca se pierde, RabbitMQ soporta acuses de recibo de mensajes. Un ack(nowledgement) es enviado de vuelta por el consumidor para decirle a RabbitMQ que un mensaje en particular ha sido recibido, procesado y que RabbitMQ es libre de borrarlo.

> Apunte: `ack` es una abreviatura de acknowledgement (reconocimiento). En el caso de que un consumidor muera (su conexión se cierre, por ejemplo) sin enviar un ack, RabbitMQ entenderá que no ha procesado el mensaje y lo reenviará a otro consumidor. Si hay otros consumidores conectados a la cola, se les enviará el mensaje.

**Acuse de recibo olvidado**

Es un error común olvidar el basic_ack. Los mensajes se volverán a entregar cuando tu cliente salga (lo que puede parecer una redistribución aleatoria), pero RabbitMQ consumirá cada vez más memoria ya que no será capaz de liberar ningún mensaje no empaquetado.

Para depurar este tipo de errores puedes usar rabbitmqctl para imprimir el campo messages_unacknowledged:

```bash
sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged
```


### Publish/Subscribe

A diferencia de las colas de trabajo, donde cada tarea se entrega a un solo trabajador, este tutorial demuestra el patrón de publicación/suscripción, que entrega mensajes a múltiples consumidores.

El ejemplo es un sistema de registro con dos programas: uno que emite mensajes de registro y otro que los recibe y los imprime.

Cada instancia del programa receptor recibe todos los mensajes, permitiendo que los registros se dirijan al disco o se visualicen en pantalla.

**Enfoque:**
A diferencia de las colas de trabajo, donde cada tarea se entrega a un solo trabajador, este tutorial demuestra el patrón de publicación/suscripción, que entrega mensajes a múltiples consumidores.

El ejemplo es un sistema de registro con dos programas: uno que emite mensajes de registro y otro que los recibe y los imprime.

Cada instancia del programa receptor recibe todos los mensajes, permitiendo que los registros se dirijan al disco o se visualicen en pantalla.

**Exchange:**
En RabbitMQ, los productores envían mensajes a un intercambio, no directamente a una cola.

Un intercambio enruta los mensajes a las colas según las reglas definidas por su tipo.

Los tipos de intercambios incluyen directo, tópico, cabeceras y fanout. El tutorial se centra en fanout, que transmite mensajes a todas las colas conocidas.

Ejemplo de declaración de un intercambio fanout:

```python
channel.exchange_declare(exchange='logs', exchange_type='fanout')
```

**Colas Temporales:**
Las colas temporales se crean con nombres generados aleatoriamente, y se eliminan automáticamente cuando se cierra la conexión del consumidor.
Ejemplo de declaración de una cola temporal:

```python
result = channel.queue_declare(queue='', exclusive=True)
```


### Routing

En el tutorial anterior, creamos un sistema de registro simple que enviaba mensajes de log a múltiples receptores. En este tutorial, añadiremos la capacidad de suscribirse solo a un subconjunto de mensajes, permitiendo, por ejemplo, que solo los mensajes de error críticos se registren en un archivo, mientras que todos los mensajes de log se imprimen en la consola.


#### Enlaces

En ejemplos anteriores, ya creamos enlaces entre intercambios (exchanges) y colas (queues). Un enlace determina qué colas están interesadas en los mensajes de un intercambio. Los enlaces pueden incluir una clave de enrutamiento (routing key) que especifica qué mensajes de un intercambio deben ser enviados a una cola.

```python
channel.queue_bind(exchange=exchange_name,
                   queue=queue_name,
                   routing_key='black')
```

La clave de enlace depende del tipo de intercambio. En un intercambio de tipo `fanout`, esta clave es ignorada. 

#### Intercambio Directo

Anteriormente, usamos un intercambio de tipo `fanout` que transmitía todos los mensajes a todos los consumidores sin distinción. Ahora utilizaremos un intercambio `direct` que permite filtrar mensajes basándose en su severidad. Así, los mensajes serán enviados solo a las colas que coincidan exactamente con la clave de enrutamiento del mensaje.

Por ejemplo, si un intercambio tiene dos colas con claves de enlace `orange` y `black`, un mensaje con clave de enrutamiento `orange` solo irá a la cola correspondiente a `orange`.

#### Múltiples Enlaces

Es posible vincular varias colas con la misma clave de enlace. En este caso, el intercambio `direct` actúa como un `fanout`, enviando el mensaje a todas las colas que tengan una clave de enlace coincidente.

#### Emisión de Logs

Usaremos este modelo para nuestro sistema de logs. En lugar de `fanout`, enviaremos mensajes a un intercambio `direct`, usando la severidad del log como clave de enrutamiento. 

Primero, debemos declarar un intercambio:

```python
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
```

Y luego podemos enviar un mensaje:

```python
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
```

Las severidades pueden ser `'info'`, `'warning'` o `'error'`.

#### Suscripción

Para recibir mensajes, crearemos un enlace para cada severidad de interés.

```python
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
```

#### Código de Ejemplo

- **`emit_log_direct.py`**: Script para emitir mensajes de log.

```python
#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(f" [x] Sent {severity}:{message}")
connection.close()
```

- **`receive_logs_direct.py`**: Script para recibir mensajes de log.

```python
#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
```

#### Ejemplos de Uso

- Para guardar solo los mensajes de `'warning'` y `'error'` en un archivo:
  ```bash
  python receive_logs_direct.py warning error > logs_from_rabbit.log
  ```

- Para ver todos los mensajes de log en pantalla:
  ```bash
  python receive_logs_direct.py info warning error
  ```

- Para emitir un mensaje de error:
  ```bash
  python emit_log_direct.py error "Run. Run. Or it will explode."
  ```


### Topics (Próximamente)





 ### RPC (Próximamente)







