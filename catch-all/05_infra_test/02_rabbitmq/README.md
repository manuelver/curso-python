# Pruebas con rabbitmq

*Índice de contenidos:*
- [Pruebas con rabbitmq](#pruebas-con-rabbitmq)
  - [Despliegue rabbitmq con docker](#despliegue-rabbitmq-con-docker)
  - [Pruebas](#pruebas)
    - [Hello World](#hello-world)
    - [Work Queues](#work-queues)
    - [Publish/Subscribe (Próximamente)](#publishsubscribe-próximamente)
    - [Routing (Próximamente)](#routing-próximamente)
    - [Topics (Próximamente)](#topics-próximamente)
    - [RPC (Próximamente)](#rpc-próximamente)


## Despliegue rabbitmq con docker

```bash
docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 -p 5672:5672 rabbitmq:3-management
```

Con [docker-compose.yaml](./docker-compose.yaml):

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

RabbitMQ habla múltiples protocolos. Este tutorial utiliza AMQP 0-9-1, que es un protocolo abierto de propósito general para mensajería. Hay un gran número de clientes para RabbitMQ en muchos idiomas diferentes. En esta serie de tutoriales vamos a usar Pika 1.0.0, que es el cliente Python recomendado por el equipo de RabbitMQ. Para instalarlo puedes usar la herramienta de gestión de paquetes pip:

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


### Publish/Subscribe (Próximamente)





### Routing (Próximamente)





### Topics (Próximamente)





 ### RPC (Próximamente)







