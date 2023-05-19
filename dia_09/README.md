# Día 9 - Programa un buscador de números de serie

## Índice
- [Día 9 - Programa un buscador de números de serie](#día-9---programa-un-buscador-de-números-de-serie)
  - [Índice](#índice)
  - [9.1. - Módulo collections](#91---módulo-collections)
  - [9.2. - Módulos shutil \& os](#92---módulos-shutil--os)
  - [9.3. - Módulo datetime](#93---módulo-datetime)
  - [9.4. - Módulo para medir el tiempo](#94---módulo-para-medir-el-tiempo)
  - [9.5. - Módulo math](#95---módulo-math)
  - [9.6. - Expresiones regulares](#96---expresiones-regulares)
  - [9.7. - Comprimir y descomprimir archivos](#97---comprimir-y-descomprimir-archivos)
  - [9.8. - Proyecto del Día 9](#98---proyecto-del-día-9)
  - [Ficheros y documentación](#ficheros-y-documentación)

## 9.1. - Módulo collections

El módulo Collections amplía los tipos de contenedores disponibles en Python. Un contenedor almacena diferentes objetos y proporciona una nueva forma de acceder e iterar sobre los mismos.

**Counters (Contadores)**: Es una subclase del **diccionario**, usado para contar las repeticiones de cada elemento en un iterable, en forma de diccionario:
```python
from collections import Counter

Counter(iterable)
```

    Counter({'valor': repeticiones, ...})

**DefaultDict**: Es una subclase del diccionario, usado para proporcionar valores por defecto para las claves que no existan, sin generar un mensaje de error. El valor por defecto puede ser un tipo de dato (int, list, etc.) o una función lambda que proporcione dicho valor directamente (lambda: "mi valor").
```python
from collections import defaultdict
mi_dic = defaultdict(lambda: "No encontrado")
```

**NamedTuple**: devuelve una tupla donde las posiciones de sus elementos tienen un nombre, además de un número de índice como las tuplas tradicionales.
```python
from collections import namedtuple

# nombres de los elementos
mi_tupla= namedtuple('Persona',['nombre','edad','altura'])
persona1 = Persona("Marcos", 39, 1.88)
```

## 9.2. - Módulos shutil & os
El módulo Shutil ofrece funcionalidades de alto nivel sobre archivos, tales como copiar, crear, eliminar y mover entre directorios. También mencionaremos métodos del módulo os que cumplen objetivos similares.
```python
import shutil
```

- **shutil.move(archivo, directorio)** : mueve un archivo desde el directorio actual hacia aquel que se especifica en el segundo parámetro.
- **os.unlink(directorio)** : elimina un archivo del directorio indicado
- **os.rmdir(directorio)** : elimina una carpeta vacía
    • shutil.rmtree(directorio) : elimina una carpeta indicada en el directorio, incluyendo todas sus ramificaciones (subcarpetas y archivos), de manera definitiva y sin pasar por la papelera de reciclaje.
- **send2trash.send2trash(archivo)** : envía un archivo a la papelera de reciclaje (es necesario instalar el módulo desde "`pip install Send2Trash`" y luego importarlo)
- **os.walk(directorio)** : recorre el directorio indicado, y devuelve los nombres de carpetas, subcarpetas y archivos dentro de ellas en forma de tupla, a través de un generador.
## 9.3. - Módulo datetime

El módulo datetime (incorporado en Python) puede importarse en proyectos para trabajar con fechas y horas, así como intervalos y duraciones.
```python
import datetime
```

fecha:
```python
mi_fecha = datetime.date(año,mes,día)
```

año,mes,día son integers comprendidos en los rangos de fechas "reales" (12 meses y 31 días como máximo). También podemos extraer el año, mes y día individualmente:
```python
anio = mi_fecha.year
mes = mi_fecha.month
dia = mi_fecha.day
```

```python
hoy = datetime.date.today()		# obtener el día actual
```

hora:
```python
mi_hora = datetime.time(hora, minuto, segundo, microsegundo)
```

Todos los argumentos son opcionales (se asumen 0 si no se indican), y deben estar comprendidos entre 0 y 24 para las horas, 0 y 60 para minutos y segundos, y 0 y 1000000 para los microsegundos.
fecha y hora:
combina fechas y horas
```python
fecha_hora = datetime.datetime(año, mes, día, hora, minuto, segundo, microseg)
ahora = datetime.datetime.now()		# obtener fecha y hora actual
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second
  #  obtener horas, minutos y segundos
```

## 9.4. - Módulo para medir el tiempo

Estudiar el tiempo transcurrido durante la ejecución de un código nos permite conocerlo mejor y tomar decisiones acerca de la vía más eficiete para resolver un problema. Tenemos dos módulos que nos ayudarán: time y timeit.

Utilizando time:
```python
	inicio = time.time()
	[código]
	final = time.time()
	duracion = final - inicio	# para funciones que toman varios segundos para ejecutarse
```

Utilizando timeit:
```python
	duracion = timeit.timeit(declaracion, setup, number = numero)
```

**declaracion**: recibe el código que cuya duración de ejecución queremos medir 
	→ es la invocación mi función

**setup**: recibe las instrucciones que el parámetro declaracion requiere para funcionar
	→ es la definición (def...) de mi función

**number**: cantidad de veces que se evaluará el código para obtener su tiempo de ejecución mínimo.
	→ pueden ser varios miles o cientos de veces (dependiendo de la complejidad)

## 9.5. - Módulo math

El módulo math contiene un conjunto de métodos y constantes que se pueden utilizar para resolver tareas matemáticas de mayor complejidad. Es el equivalente a la calculadora científica dentro de Python.
Algunas de las situaciones que pueden ayudarnos a resolver son:

- **Relaciones trigonométricas** (seno, coseno, tangente, sus inversas e hiperbólicas) 
- **Funciones logarítmicas** 
- **Potencias y raíces** 
- **Combinatoria y permutaciones**
- **Redondeos**
- **Factoriales**

... entre muchas otras (¡te recomendamos leer su documentación de acuerdo con tus necesidades!)

Las constantes que encontrarás:
- **Pi** (3.1415...)
- **e o Constante de Euler** (2.7182...)
- **Tau** (6.2831...)
- **Infinito** (el concepto matemático de infinito positivo)
- **Nulo** (NaN: not-a-number)

## 9.6. - Expresiones regulares

Una expresión regular es una secuencia de caracteres que forman un patrón de búsqueda determinado. Pueden ser utilizadas para verificar strings en búsqueda de un contenido (patrón) específico. Utilizamos el módulo re en Python.
```python
import re
```

Funciones:
- **search( )**: devuelve un objeto "match" que contiene información acerca del hallazgo si se encuentra en algún punto del string
- **findall( )**: devuelve una lista que contiene todos los hallazgos del patrón

Para formar patrones, utilizamos los siguientes cuantificadores y caracteres especiales.

**Operadores especiales:**

| Operador | Descripción            |
| :------: | :--------------------- |
|   [ ]    | Un set de caracteres   |
|    .     | Un carácter cualquiera |
|    ^     | Inicia con             |
|    $     | Finaliza con           |
|    \|    | Operador lógico "O"    |

**Cuantificadores: **

| Cuantificador | Descripción                           |
| :-----------: | :------------------------------------ |
|       *       | Cero o más ocurrencias: 0 – n         |
|       +       | Una o más ocurrencias: 1 – n          |
|       ?       | Cero o una ocurrencia: 0 – 1          |
|      { }      | Un número especificado de ocurrencias |
|      {n}      | Se repite n veces                     |
|     {n,m}     | Se repite de n a m veces              |
|     {n, }     | Se repite de n veces hacia arriba     |

**Carácteres especiales:**

| Carácter  | Descripción                  |
| :-------: | :--------------------------- |
|    \d     | Dígito numérico              |
|    \D     | NO numérico                  |
|    \w     | Carácter alfanumérico        |
|    \W     | NO alfanumérico              |
|    \s     | Espacio en blanco            |
|    \S     | NO espacio en blanco         |
|  patron   | r'\w{4}\d{4}'                |
| verificar | re.search(patron,"cont1234") |

Expresiones regulares python online: https://pythex.org/ 

## 9.7. - Comprimir y descomprimir archivos

El formato zip permite comprimir archivos sin pérdida de información, ahorrando espacio de almacenamiento y manteniendo documentos relacionados en un mismo archivo .zip.

Utilizando el módulo zipfile:
```python
	import zipfile
```

Comprimir archivos:
```python
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")		# modo escritura
mi_zip.write("mi_archivo.txt")		# comprimir archivo en mi_zip
mi_zip.close()
```

Descomprimir archivos:
```python
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "r")
mi_zip.extractall()			# extraer todos los archivos de mi_zip
mi_zip.extract("mi_archivo.txt")	# extraer un archivo específico
```

Utilizando el módulo shutil:
```python
import shutil
```

Comprimir archivos:
```python
shutil.make_archive(archivo_destino, "zip", carpeta_origen)
```

Descomprimir archivos:
```python
shutil.unpack_archive(archivo_zip, nombre_carpeta_extraccion, "zip")
```

## 9.8. - Proyecto del Día 9

A esta altura del día ya estoy un poco cansado, así que vamos a hacer algo distinto en esta ocasión. Esta vez, en vez de explicarte los detalles del proyecto del día de hoy, los vas a tener que encontrar tú mismo.

Junto a esta lección, vas a encontrar un archivo zip descargable. Descárgalo, guárdalo en la misma carpeta donde vas a guardar tus archivos de Python para este proyecto, y luego quiero que descomprimas ese archivo para encontrar las consignas del proyecto de hoy. Pero no hagas trampa: la idea es que descomprimas ese archivo usando el código que has aprendido el día de hoy, y lo que vas a encontrar ahí, es un archivo llamado Instrucciones. Ese archivo tiene todo lo que necesitas para ponerte a trabajar.

Así que manos a la obra, y nos vemos en un rato para mostrarte mi solución al proyecto del día de hoy.

## Ficheros y documentación

- [01_modulo_collections.py](01_modulo_collections.py)
- [02_modulo_os_shutil.py](02_modulo_os_shutil.py)
- [03_modulo_datetime_1.py](03_modulo_datetime_1.py)
- [03_modulo_datetime_2.py](03_modulo_datetime_2.py)
- [04_modulo_medir_tiempo.py](04_modulo_medir_tiempo.py)
- [05_modulo_math.py](05_modulo_math.py)
- [06_modulo_re.py](06_modulo_re.py)
- [07_modulo_comprimir_shutil.py](07_modulo_comprimir_shutil.py)
- [07_modulo_comprimir_zipfile.py](07_modulo_comprimir_zipfile.py)
- [07_modulo_descomprimir_shutil.py](07_modulo_descomprimir_shutil.py)
- [07_modulo_descomprimir_zipfile.py](07_modulo_descomprimir_zipfile.py)
- [08_Descomprimir_proyecto.py](08_Descomprimir_proyecto.py)
- [09_Programa09](09_Programa09.py)
- [carpeta_superior](carpeta_superior)
- [extraccion_terminada](extraccion_terminada)
- [mi_texto_A.txt](mi_texto_A.txt)
- [mi_texto_B.txt](mi_texto_B.txt)
- [Proyecto+Dia+9.zip](Proyecto+Dia+9.zip)
- [todo_comprimido.zip](todo_comprimido.zip)

[Documentación curso](../doc_curso/09_buscador_numeros_serie/)
