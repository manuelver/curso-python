# Día 13 - Programa un asistente de voz

## Índice
- [Día 13 - Programa un asistente de voz](#día-13---programa-un-asistente-de-voz)
  - [Índice](#índice)
  - [13.1. - Librerias y módulos](#131---librerias-y-módulos)
  - [13.2. - Algunos problemas con las bibliotecas](#132---algunos-problemas-con-las-bibliotecas)
    - [13.2.1. - Problemas con Flask](#1321---problemas-con-flask)
    - [13.2.2. - Problemas con PyAudio](#1322---problemas-con-pyaudio)
      - [13.2.2.1. -     Solución 1](#13221-------solución-1)
      - [13.2.2.2. -     Solución 2](#13222-------solución-2)
      - [13.2.2.3. -     Solución 3](#13223-------solución-3)
      - [13.2.2.4. -     Solución 4](#13224-------solución-4)
      - [13.2.2.5. -     Solución 5](#13225-------solución-5)
  - [13.3. - Enlaces](#133---enlaces)
  - [Ficheros y documentación](#ficheros-y-documentación)

## 13.1. - Librerias y módulos

- **pyttsx3**: Librería de síntesis de voz en Python. Permite convertir texto en voz humana de forma programática utilizando diferentes voces y ajustes.
- **speech_recognition**: Librería para reconocimiento de voz en Python. Permite grabar voz desde un micrófono o cargar un archivo de audio, y convertirlo en texto utilizando tecnologías de reconocimiento de voz. pip install SpeechRecognition
- **webbrowser**: Módulo de Python que permite controlar el navegador web del SO. Permite abrir páginas web, buscar en Internet y realizar otras acciones relacionadas con la navegación web.
- **pywhatkit**: Librería de Python que proporciona una interfaz de alto nivel para realizar tareas comunes en la web, como búsqueda en Google, envío de mensajes de WhatsApp, reproducción de vídeos de YouTube y otras tareas similares.
- **yfinance**: Librería de Python para acceder a datos financieros de Yahoo Finance. Permite descargar y analizar datos históricos de precios de acciones, índices y otros recursos financieros.
- **pyjokes**: Librería de Python que proporciona una colección de chistes en inglés. Los chistes se pueden utilizar para hacer programas más divertidos o para fines de aprendizaje de idiomas.
- **wikipedia**: es una librería de Python que permite acceder a la enciclopedia en línea Wikipedia. Permite buscar y recuperar información detallada sobre temas específicos, así como interactuar con la API de Wikipedia.

## 13.2. - Algunos problemas con las bibliotecas

### 13.2.1. - Problemas con Flask

Si al ejecutar el código de la lección "Transformar Voz en Texto" recibes el siguiente mensaje de error:
```shell
ModuleNotFoundError: No module named 'flask'
```

Esto simplemente se soluciona instalando la biblioteca Flask con el siguiente comando:
```shell
pip install flask
```

### 13.2.2. - Problemas con PyAudio

Aunque no vamos a instalar manualmente la biblioteca PyAudio, sí vamos a instalar otra biblioteca (SpeechRecognition) que al ejecutarse se encarga de instalar PyAudio sin que lo veamos en pantalla. Curiosamente PyAudio no siempre se instala como corresponde y esto le está trayendo dolores de cabeza a más de un estudiante.

Si al ejecutar el código de la lección "Transformar Voz en Texto" recibes el siguiente mensaje de error:
```shell
AttributeError("Could not find PyAudio; chack installation")
```

en ese caso, la forma de resolverlo es instalar PyAudio manualmente, pero esto no siempre resulta como debería, por lo que a continuación voy a compartir contigo las diferentes soluciones que están dando resultado. Intenta con cada una de ellas en orden hasta que alguna te de resultado.

#### 13.2.2.1. -     Solución 1

Abre CMD en Windows (o la terminal en Mac) y escribe lo siguiente:
```shell
pip install PyAudio
```

#### 13.2.2.2. -     Solución 2

1. En PyCharm ve a `File / Settings / Project: Python / Python Interpreter`
2. Click en +
3. En la barra de búsquedas escribe "PyAudio"
4. Selecciona el resultado correcto y haz click en Install Package

#### 13.2.2.3. -     Solución 3

Abre CMD en Windows (o la terminal en Mac) y escribe lo siguiente:
```shell
pip install pipwin
pipwin install PyAudio
```

#### 13.2.2.4. -     Solución 4

1. En PyCharm ve a View / Tool Windows / Terminal
2. Escribe lo siguiente:
    ```shell
    pip install pipwin
    pipwin install PyAudio
    ```

#### 13.2.2.5. -     Solución 5 

1. Asegúrate de conocer la versión de python que tienes instalada. Puedes verificarlo escribiendo lo siguiente en la terminal:
    ```shell
    python --version
    ```
    Obtendrás, por ejemplo:

        Python 3.10.0

2. Comprueba qué versión de Python tienes instalada (32 o 64 bits). La manera más sencilla es escribir en la terminal lo siguiente:
    ```shell
    python
    ```
    De esta manera obtendrás, entre otra información, algo parecido a lo siguiente, que se muestra en mi caso

        MSC v.1927 64 bit (AMD64)] on win32.

    Lo importante es lo resaltado entre paréntesis. Toma nota de lo que obtienes al hacerlo tú.

3. De acuerdo con lo anterior, en mi ordenador tendría que instalar una versión de PyAudio para Python 3.10 (310) de 64 bits (win_amd64). Nuevamente, puede no ser la misma versión que necesites tú.

4. Ingresa en este enlace https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio , y dirígete al encabezado que dice PyAudio: bindings for the PortAudio library.

5. Ahí encontrarás listados varios archivos que se usan para reemplazar la versión de PyAudio que ofrece PyPi. Debes elegir la que corresponde a tu ordenador y a tu versión de Python (según los datos que te enseñé a rocoger en los puntos 1 y 2 de esta solución). En mi caso tendría que descargar la siguiente versión:

    `PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl`

    Descarga la que necesites tú de acuerdo a lo verificado en los puntos 1 y 2.

6. Localiza la carpeta de descargas en donde se haya bajado el archivo. Por ejemplo en mi caso:
    ```shell
    C:\Users\Win10\Downloads
    ```

7. Abre la terminal y escribe:
    ```shell
    cd C:\Users\Usuario\Downloads
    ```

8. A continuación escribe en la terminal lo siguiente:
    ```shell
    pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
    ```

    (deberás reemplazar el nombre del archivo descargado por el que hayas bajado tú).

9. Esto habrá instalado PyAudio y solucionará tu problema.

## 13.3. - Enlaces
Instrucciones para descargar idiomas en Windows: https://support.microsoft.com/es-es/topic/descargar-idiomas-y-voces-para-lector-inmersivo-el-modo-lectura-y-lectura-en-voz-alta-4c83a8d8-7486-42f7-8e46-2b0fdf753130

Instrucciones para cambiar el idioma en Mac:
https://support.apple.com/es-es/guide/mac-help/mh26684/mac#:~:text=En%20el%20Mac%2C%20selecciona%20el,en%20%E2%80%9CIdioma%20y%20regi%C3%B3n%E2%80%9D%20.&text=Haz%20clic%20en%20General.,y%20haz%20clic%20en%20A%C3%B1adir.

## Ficheros y documentación
- [asistente_virtual.py](asistente_virtual.py)

[Documentación del día](../doc_curso/13_asistente_voz/)

---

Enlaces a todos los días: [dia 1 - creador de nombres](../dia_01/README.md) / [dia 2 - calculador de comisiones](../dia_02/README.md) / [dia 3 - analizador de texto](../dia_03/README.md) / [dia 4 - juego "adivina el número"](../dia_04/README.md) / [dia 5 - juego "El ahorcado"](../dia_05/README.md) / [dia 6 - recetario](../dia_06/README.md) / [dia 7 - cuenta bancaria](../dia_07/README.md) / [dia 8 - consola de turnos](../dia_08/README.md) / [dia 9 - buscador de números de serie](../dia_09/README.md) / [dia 10 - juego "Invasión espacial"](../dia_10/README.md) / [dia 11 - web scraping](../dia_11/README.md) / [dia 12 - gestor de restaurantes](../dia_12/README.md) / [dia 13 - asistente de voz](../dia_13/README.md) / [dia 14 - controlador de asistencia](../dia_14/README.md) / [dia 15 - machine learning](../dia_15/README.md) / [dia 16 - aplicación web de tareas pendientes](../dia_16/README.md)
