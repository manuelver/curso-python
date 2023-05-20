"""
Programa dia 13 - Asistente virtual

Bibliotecas:
    cmake 
    dlib
    face-recognition
    numpy
    opencv-python

"""

import os
import cv2
import face_recognition as fr
import numpy
from datetime import datetime

# Crear base de datos
ruta = 'Empleados'
mis_imagenes = []
# Obtener nombres de las fotos
nombre_empleados = []
# Nombres con la extensión .jpg
lista_empleados = os.listdir(ruta)


# Cargar imágenes con loop
for nombre in lista_empleados:

    # Leer la imagen
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')

    # Añadimos las coordenadas de la imagen en una nueva lista
    mis_imagenes.append(imagen_actual)

    # Añadimos tan solo el nombre del empleado
    nombre_empleados.append(os.path.splitext(nombre)[0])

# Mostrar lista creada
print(nombre_empleados)


def codificar(imagenes):
    """ Codificar las imágenes """
    # Crear una lista nueva
    lista_codificada = []

    # Loop para procesar las imágenes
    for imagen in imagenes:
        # Pasar imágenes a RGB
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # Codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregar a la lista codificada
        lista_codificada.append(codificado)

    # Devolver lista codificada que se ha procesado
    return lista_codificada


def registrar_ingresos(persona):
    """ Recoger los datos de las capturas """

    # Creamos el fichero registro.csv con Nombre, Hora
    # Aquí lo abrimos para leer
    f = open('registro.csv', 'r+')
    # Hacemos un listado con las líneas del fichero
    lista_datos = f.readlines()
    # Lista vacía para almacenar los registros
    nombres_registro = []

    for linea in lista_datos:
        # leemos separando por comas
        ingreso = linea.split(',')
        # Añadimos a la lista
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:

        # Determinamos la hora actual
        ahora = datetime.now()
        # Le damos formato a la hora
        string_ahora = ahora.strftime('%H:%M:%S')

        # Escribimos la persona
        f.writelines(f'\n{persona}, {string_ahora}')


# Llamar a la función
lista_empleados_codificada = codificar(mis_imagenes)


# Mostrar número de imágenes codificadas en la función
# print(len(lista_empleados_codificada))


# Tomar una imágen de cámara web
captura = cv2.VideoCapture(0)

# Configuración de la captura para Linux
captura.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
sleep = 'sleep 3'
os.system(sleep)
captura.set(cv2.CAP_PROP_EXPOSURE, -8.0)

# Leer la imágen de la cámara
# El método read() arroja dos elementos:
# - Si se ha podido realizar la captura
# - Devuelve la imágen
exito, imagen = captura.read()

if not exito:
    print('No se pudo tomar la captura')
else:
    # Primero intentamos reconocer la cara en captura
    cara_captura = fr.face_locations(imagen)

    # Codificar la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Busquemos coincidencias entre las imágenes capturadas
    # y la lista de imágenes de empleados
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        # Comparación
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)

        # Distancias de comparación
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        # La distancia menor de la lista "distancias"
        # será la que indique el parecido más cercano
        print(distancias)

        # Buscar el valor mínimo y añadir a variable
        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencias si las hay
        if distancias[indice_coincidencia] > 0.6:
            texto = 'No coincide'

        else:

            # Buscar el nombre del empleado encontrado
            texto = nombre_empleados[indice_coincidencia]

        # Crear rectangulo cara
        y1, x2, y2, x1 = caraubic
        cv2.rectangle(
            imagen,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )
        # Crear rectangulo verde de texto
        cv2.rectangle(
            imagen,
            (x1, y2 - 35),
            (x2, y2),
            (0, 255, 0),
            cv2.FILLED
        )

        # Crear texto
        cv2.putText(
            imagen,
            texto,
            (x1 + 6, y2 - 6),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        registrar_ingresos(nombre)

        # Mostrar la imagen obtenida por la cámara
        cv2.imshow('Imagen web', imagen)

        # Mantener la ventana abierta
        cv2.waitKey(0)
