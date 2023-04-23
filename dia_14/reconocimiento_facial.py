"""
Reconocimiento facial

Bibliotecas:
    cmake 
    dlib
    face-recognition
    numpy
    opencv-python

"""

import cv2
import face_recognition as fr

# Cargar imágenes
foto_control = fr.load_image_file('FotoD.jpg')
foto_prueba = fr.load_image_file('FotoC.jpg')

# Nos aseguramos que el formato de la foto es rgb
# Las transformamos de BGR --> RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
# Podríamos ver las coordenadas
# print(lugar_cara_A)

# Codificar la cara
cara_codificada_A = fr.face_encodings(foto_control)[0]


# Localizar cara control
lugar_cara_B = fr.face_locations(foto_prueba)[0]

# Codificar la cara
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# Marcar donde está la cara con un rectángulo
# Añadimos la foto y los índices para marcar las coordenadas
# del vértice superior izquiero de la cara y el
# del vértice inferior derecho.
# Anadimos el color del rectangulo en verde
# y el borde
cv2.rectangle(
    foto_control,
    (lugar_cara_A[3], lugar_cara_A[0]),
    (lugar_cara_A[1], lugar_cara_A[2]),
    (0, 255, 0),
    2
)

cv2.rectangle(
    foto_prueba,
    (lugar_cara_B[3], lugar_cara_B[0]),
    (lugar_cara_B[1], lugar_cara_B[2]),
    (0, 255, 0),
    2
)


# Realizar comparación
# El método espera recibir una lista.
# Como tenemos un único objecto lo ponemos entre corchetes
# para que piense que es una lista de un solo objeto.
# El tercer valor es la torelancia de distancia de comparación
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)
# print(resultado)


# Medida de la distancia de comparación
# por defecto es 0.6 el valor para admitir coincidencia con True
# Esto nos indica lo cerca que está
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
# print(distancia)


# Mostrar resultado con texto
# Los parámetros son la imagén, el texto a introducir,
# la ubicación del texto, la fuente, la escala,
# el color y el grosor
cv2.putText(
    foto_prueba,
    f'{resultado} {distancia.round(2)}',
    (50, 50),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (0, 255, 0),
    2
)


# Mostrar imágenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Las imágenes se cierran, se necesitan mantener el programa abierto
cv2.waitKey(0)
