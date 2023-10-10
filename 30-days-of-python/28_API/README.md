# API

Documento original en inglés: [API](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/28_Day_API/28_API.md)

## Ejercicios

1. Lee sobre API y HTTP:

### Interfaz de programación de aplicaciones (API)

#### API

El tipo de API que vamos a ver son las API Web. Son las interfaces definidas a través de las cuales se producen las interacciones entre una empresa y las aplicaciones que utilizan sus activos, que también es un Acuerdo de Nivel de Servicio (SLA) para especificar el proveedor funcional y exponer la ruta de servicio o URL para los usuarios de la API.

En el contexto del desarrollo web, una API se define como un conjunto de especificaciones, como los mensajes de solicitud del Protocolo de Transferencia de Hipertexto (HTTP), junto con una definición de la estructura de los mensajes de respuesta, normalmente en un formato XML o de Notación de Objetos JavaScript (JSON).

Las API web se han ido alejando de los servicios web basados en el Protocolo Simple de Acceso a Objetos (SOAP) y la arquitectura orientada a servicios (SOA) para acercarse más directamente a los recursos web de estilo de transferencia de estado representacional (REST).

Los servicios de medios sociales, las API web han permitido a las comunidades web compartir contenidos y datos entre comunidades y distintas plataformas.

Gracias a las API, los contenidos creados en un lugar pueden publicarse y actualizarse dinámicamente en varios sitios de la web.

Por ejemplo, la API REST de Twitter permite a los desarrolladores acceder a los datos básicos de Twitter y la API de búsqueda proporciona métodos para que los desarrolladores interactúen con los datos de búsqueda y tendencias de Twitter.

Muchas aplicaciones proporcionan puntos finales de API. Algunos ejemplos de API son la [API de países](https://restcountries.eu/rest/v2/all) o la [API de razas de gatos](https://api.thecatapi.com/v1/breeds). 

Vamos a ver una API RESTful que utiliza métodos de solicitud HTTP para GET, PUT, POST y DELETE de datos.

#### Creación de API

RESTful API es una interfaz de programación de aplicaciones (API) que utiliza peticiones HTTP para GET, PUT, POST y DELETE de datos. En las secciones anteriores, hemos aprendido sobre python, flask y mongoDB. Utilizaremos los conocimientos adquiridos para desarrollar una API RESTful utilizando Python flask y la base de datos mongoDB. Toda aplicación que tenga operaciones CRUD (Create, Read, Update, Delete) tiene una API para crear datos, obtener datos, actualizar datos o borrar datos de una base de datos.

Para construir una API, es bueno entender el protocolo HTTP y el ciclo de petición y respuesta HTTP.

##### HTTP(Protocolo de transferencia de hipertexto)

HTTP es un protocolo de comunicación establecido entre un cliente y un servidor. Un cliente en este caso es un navegador y el servidor es el lugar donde se accede a los datos. HTTP es un protocolo de red utilizado para entregar recursos que pueden ser archivos en la World Wide Web, ya sean archivos HTML, archivos de imagen, resultados de consultas, scripts u otros tipos de archivos.

Un navegador es un cliente HTTP porque envía peticiones a un servidor HTTP (servidor Web), que a su vez envía respuestas al cliente.

##### Estructura de HTTP

HTTP utiliza el modelo cliente-servidor. Un cliente HTTP abre una conexión y envía un mensaje de solicitud a un servidor HTTP y el servidor HTTP devuelve un mensaje de respuesta que contiene los recursos solicitados. Cuando finaliza el ciclo de respuesta a la solicitud, el servidor cierra la conexión.

![](https://github.com/Asabeneh/30-Days-Of-Python/raw/master/images/http_request_response_cycle.png)

El formato de los mensajes de solicitud y respuesta es similar. Ambos tipos de mensajes tienen

- una línea inicial,
- cero o más líneas de encabezamiento,
- una línea en blanco (es decir, un CRLF solo), y
- un cuerpo de mensaje opcional (por ejemplo, un archivo, o datos de consulta, o salida de consulta).

Veamos un ejemplo de mensajes de solicitud y respuesta navegando por este [sitio](https://thirtydaysofpython-v1-final.herokuapp.com/). Este sitio ha sido desplegado en Heroku free dyno y en algunos meses puede no funcionar debido a la alta solicitud. Apoyar este trabajo para que el servidor funcione todo el tiempo.

![](https://github.com/Asabeneh/30-Days-Of-Python/raw/master/images/request_response_header.png)


#### Línea de solicitud inicial (línea de estado)

La línea de solicitud inicial es diferente de la respuesta. Una línea de petición tiene tres partes, separadas por espacios:

- nombre del método (GET, POST, HEAD)
- ruta del recurso solicitado,
- la versión de HTTP utilizada. ej. GET / HTTP/1.1

GET es el HTTP más común que ayuda a obtener o leer recursos y POST es un método de solicitud común para crear recursos.
Línea de respuesta inicial (línea de estado)

La línea de respuesta inicial, llamada línea de estado, también tiene tres partes separadas por espacios:

- Versión HTTP
- Código de estado de la respuesta que da el resultado de la petición, y una razón que describe el código de estado. Ejemplos de líneas de estado son: HTTP/1.0 200 OK o HTTP/1.0 404 No encontrado Notas:

Los códigos de estado más comunes son: 200 OK: La solicitud se ha realizado correctamente y el recurso resultante (por ejemplo, un archivo o la salida de un script) se devuelve en el cuerpo del mensaje. 500 Error de servidor Puede encontrar una lista completa de códigos de estado HTTP aquí. También se puede encontrar aquí.

##### Campos de cabecera

Como se ve en la captura de pantalla anterior, las líneas de cabecera proporcionan información sobre la solicitud o la respuesta, o sobre el objeto enviado en el cuerpo del mensaje.

```
GET / HTTP/1.1
Host: thirtydaysofpython-v1-final.herokuapp.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Referer: https://thirtydaysofpython-v1-final.herokuapp.com/post
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9,fi-FI;q=0.8,fi;q=0.7,en-CA;q=0.6,en-US;q=0.5,fr;q=0.4
```

##### El cuerpo del mensaje

Un mensaje HTTP puede tener un cuerpo de datos que se envía después de las líneas de cabecera. En una respuesta, es donde se devuelve al cliente el recurso solicitado (el uso más común del cuerpo del mensaje), o quizás un texto explicativo si hay un error. En una solicitud, es donde se envían al servidor los datos introducidos por el usuario o los archivos cargados.

Si un mensaje HTTP incluye un cuerpo, normalmente hay líneas de encabezado en el mensaje que describen el cuerpo. En particular,

La cabecera Content-Type: indica el tipo MIME de los datos del cuerpo (text/html, application/json, text/plain, text/css, image/gif). La cabecera Content-Length: indica el número de bytes del cuerpo.
Métodos de solicitud

GET, POST, PUT y DELETE son los métodos de petición HTTP con los que vamos a implementar una API o una aplicación de operaciones CRUD.

1. GET: El método GET se utiliza para recuperar y obtener información del servidor dado utilizando un URI dado. Las peticiones que utilizan GET sólo deben recuperar datos y no deben tener ningún otro efecto sobre los datos.

2. POST: La petición POST se utiliza para crear datos y enviarlos al servidor, por ejemplo, crear un nuevo post, subir archivos, etc. utilizando formularios HTML.

3. PUT: Sustituye todas las representaciones actuales del recurso de destino por el contenido subido y lo utilizamos modificar o actualizar datos.

4. DELETE: Elimina datos


[<< Day 27](../27_Python_con_MongoDB/README.md) | [Day 29 >>](../29_Construcción_de_API/README.md)
