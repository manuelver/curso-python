# Día 14 - Programa un controlador de asistencia

**Paso 1** – Reconocimiento facial

**Paso 2** – Análisis facial

**Paso 3** – Convertir la imágen en datos

hog → Histograms of oriented gradients for human detection https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients 

Vscode: https://visualstudio.microsoft.com/es/downloads/

## Índice
- [Día 14 - Programa un controlador de asistencia](#día-14---programa-un-controlador-de-asistencia)
  - [Índice](#índice)
  - [14.1. - Bibliotecas](#141---bibliotecas)
  - [Ficheros y documentación](#ficheros-y-documentación)

## 14.1. - Bibliotecas

- **cmake**: es una biblioteca de software que se utiliza para construir y compilar aplicaciones de software. Es muy útil para proyectos que tienen dependencias y para proyectos que deben compilarse en diferentes sistemas operativos. *Documentación de CMake*: https://cmake.org/documentation/
- **dlib**: es una biblioteca de procesamiento de imágenes y aprendizaje automático en C++ que se puede utilizar en Python. Es muy utilizada en aplicaciones de reconocimiento facial, detección de objetos y seguimiento de objetos. *Documentación de dlib*: http://dlib.net/documentation.html
- **face**-recognition: es una biblioteca de Python basada en dlib, que permite detectar y reconocer caras en imágenes y vídeos. Utiliza técnicas de aprendizaje automático para identificar características faciales únicas, y es muy útil en aplicaciones de seguridad, reconocimiento de personas y análisis de imágenes. *Documentación de face-recognition*: https://face-recognition.readthedocs.io/en/latest/
- **numpy**: es una biblioteca de Python para computación científica que se utiliza para realizar operaciones matemáticas en matrices y vectores. Es muy útil en aplicaciones de análisis de datos, aprendizaje automático, procesamiento de señales y otras áreas de la ciencia y la ingeniería. *Documentación de NumPy*: https://numpy.org/doc/
- **opencv-python**: es una biblioteca de procesamiento de imágenes y vídeo en Python. Proporciona funciones para leer, escribir y procesar imágenes y vídeos, así como para realizar operaciones avanzadas como reconocimiento facial, detección de objetos y seguimiento de objetos. *Documentación de OpenCV (Python)*: https://docs.opencv.org/master/

Para instalar estas bibliotecas en Ubuntu, hay varias opciones:
- Con el comando `sudo apt-get install` seguido del nombre del paquete.
- Con el comando `pip install` seguido del nombre de la biblioteca.
- Con el comando `conda install` seguido del nombre de la biblioteca.


Cuando realizamos la comparación de las imágenes, con las caras codificadas y mediante el código:
```python
fr.compare_faces(lista_imagenes, imagen_a_comparar)
```

Tienen un valor True cuando tiene un valor de 0.6 (Valor por defecto) en el punto de comparación (La distancia entre ambas caras)

Los ficheros .csv se llaman así por Comma-Separated Values" (Valores separados por comas), lo que indica que se trata de un formato de archivo en el que los datos están separados por comas.


## Ficheros y documentación

- [asistencia.py](asistencia.py)
- [Empleados](Empleados/)
- [FotoA.jpg](FotoA.jpg)
- [FotoB.jpg](FotoB.jpg)
- [FotoC.jpg](FotoC.jpg)
- [FotoD.jpg](FotoD.jpg)
- [reconocimiento_facial.py](reconocimiento_facial.py)
- [registro.csv](registro.csv)

[Documentación del día](../doc_curso/14_asistencia/)

---

Enlaces a todos los días: [dia 1 - creador de nombres](../dia_01/README.md) / [dia 2 - calculador de comisiones](../dia_02/README.md) / [dia 3 - analizador de texto](../dia_03/README.md) / [dia 4 - juego "adivina el número"](../dia_04/README.md) / [dia 5 - juego "El ahorcado"](../dia_05/README.md) / [dia 6 - recetario](../dia_06/README.md) / [dia 7 - cuenta bancaria](../dia_07/README.md) / [dia 8 - consola de turnos](../dia_08/README.md) / [dia 9 - buscador de números de serie](../dia_09/README.md) / [dia 10 - juego "Invasión espacial"](../dia_10/README.md) / [dia 11 - web scraping](../dia_11/README.md) / [dia 12 - gestor de restaurantes](../dia_12/README.md) / [dia 13 - asistente de voz](../dia_13/README.md) / [dia 14 - controlador de asistencia](../dia_14/README.md) / [dia 15 - machine learning](../dia_15/README.md) / [dia 16 - aplicación web de tareas pendientes](../dia_16/README.md)
