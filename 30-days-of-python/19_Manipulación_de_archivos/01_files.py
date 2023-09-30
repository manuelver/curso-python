"""
01_files.py
"""
import os
import json
import nltk
import re
from data.stop_words import stop_words

# Ejercicio: Nivel 1

# 1. Escribe una función que cuente el número
# de líneas y palabras en un texto.
# Todos los archivos se encuentran en la carpeta [data](./data)):


def contar_lineas_palabras(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        f.seek(0)
        palabras = f.read().split()
        # Contar palabras

        resultado = f'tiene {len(lineas)} lineas y {len(palabras)} palabras\n'

        return resultado

# a) Lee el archivo obama_speech.txt
# y cuenta el número de líneas y palabras


print(
    f"El discurso de Obama {contar_lineas_palabras('data/obama_speech.txt')}")

# b) Lee el archivo michelle_obama_speech.txt
# y cuenta el número de líneas y palabras

print(
    f"El discurso de Michelle {contar_lineas_palabras('data/michelle_obama_speech.txt')}")

# c) Lee el archivo donald_speech.txt
# y cuenta el número de líneas y palabras

print(
    f"El discurso de Donald {contar_lineas_palabras('data/donald_speech.txt')}")

# d) Lee el archivo melina_trump_speech.txt
# y cuenta el número de líneas y palabras

print(
    f"El discurso de Melina {contar_lineas_palabras('data/melina_trump_speech.txt')}")


# 2. Lee el archivo de datos countries_data.json
# en el directorio data,
# crea una función que encuentre
# los diez idiomas más hablados.


def diez_idiomas_mas_hablados():
    archivo = 'data/countries_data.json'
    with open(archivo, 'r') as f:
        data = json.load(f)
        idiomas = []
        for pais in data:
            idiomas.extend(pais['languages'])

        # Contamos la frecuencia de cada idioma
        idiomas_freq = {}
        for idioma in idiomas:
            if idioma in idiomas_freq:
                idiomas_freq[idioma] += 1
            else:
                idiomas_freq[idioma] = 1

        # Ordenamos los idiomas por frecuencia
        # y tomamos los 10 más comunes
        diez_idiomas = sorted(
            idiomas_freq.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        # Creamos una lista de tuplas
        # que contengan el nombre del idioma
        # y el número de países en los que se habla
        resultado = []
        for idioma, frecuencia in diez_idiomas:
            resultado.append((idioma, frecuencia))

        return resultado


for idioma, frecuencia in diez_idiomas_mas_hablados():
    print(f"{idioma} se habla en {frecuencia} paises")

print()

# 3. Lee el archivo de datos countries_data.json
# en el directorio data,
# crea una función que genere
# una lista de los diez países más poblados.


def diez_paises_mas_poblados():
    archivo = 'data/countries_data.json'
    with open(archivo, 'r') as f:
        data = json.load(f)
        paises = []
        for pais in data:
            paises.append((pais['name'], pais['population']))

        # Ordenamos los paises por población
        # y tomamos los 10 más poblados
        diez_paises = sorted(
            paises,
            key=lambda x: x[1],
            reverse=True
        )[:10]

        resultado = []
        for pais, poblacion in diez_paises:
            poblacion_millones = poblacion / 1000000
            resultado.append((pais, poblacion_millones))

        return resultado


for pais, poblacion in diez_paises_mas_poblados():
    print(f"{pais} tiene {poblacion:.2f} millones de habitantes")

print()

# Ejercicios: Nivel 2

# 1. Extrae todas las direcciones
# de correo electrónico entrantes
# como una lista del archivo
# email_exchange_big.txt.


def extraer_correos():
    archivo = 'data/email_exchanges_big.txt'
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        correos = {}
        for linea in lineas:
            if linea.startswith('From '):
                correo = linea.split()[1]
                if correo in correos:
                    correos[correo] += 1
                else:
                    correos[correo] = 1

        return correos


for correo, frecuencia in extraer_correos().items():
    print(f"{correo} envió {frecuencia} correos")

print()

# 2. Encuentra las palabras más comunes
# en el idioma inglés.
# Llama a tu función encontrar_palabras_mas_comunes,
# tomará dos parámetros:
# una cadena o un archivo
# y un número entero positivo
# que indicará la cantidad de palabras.
# Tu función devolverá una lista de tuplas
# en orden descendente.


def encontrar_palabras_mas_comunes(archivo, n):
    with open(archivo, 'r') as f:
        palabras = f.read().split()

        # Etiquetamos cada palabra con su POS
        palabras_pos = nltk.pos_tag(palabras)

        # Filtramos las palabras que sean sustantivos o verbos
        palabras_filtradas = []
        for palabra, pos in palabras_pos:
            if pos.startswith('N') or pos.startswith('V'):
                palabras_filtradas.append(palabra)

        # Contamos las palabras filtradas
        palabras_freq = {}
        for palabra in palabras_filtradas:
            if palabra in palabras_freq:
                palabras_freq[palabra] += 1
            else:
                palabras_freq[palabra] = 1

        # Ordenamos las palabras por frecuencia
        # y tomamos las n más comunes
        n_palabras = sorted(
            palabras_freq.items(),
            key=lambda x: x[1],
            reverse=True
        )[:n]

        # Creamos una lista de tuplas
        # que contengan el nombre de la palabra
        # y el número de veces que aparece
        resultado = []
        for palabra, frecuencia in n_palabras:
            resultado.append((palabra, frecuencia))

        return resultado


for palabra, frecuencia in encontrar_palabras_mas_comunes('data/romeo_and_juliet.txt', 10):
    print(f"\"{palabra}\" aparece {frecuencia} veces")

print()

# 3. Utiliza la función encontrar_palabras_mas_comunes para encontrar:
# a) Las diez palabras más frecuentes utilizadas en el discurso de Obama
print('Las diez palabras más frecuentes utilizadas en el discurso de Obama')
for palabra, frecuencia in encontrar_palabras_mas_comunes('data/obama_speech.txt', 10):
    print(f"\"{palabra}\" aparece {frecuencia} veces")

print()

# b) Las diez palabras más frecuentes utilizadas en el discurso de Michelle
print('Las diez palabras más frecuentes utilizadas en el discurso de Michelle')
for palabra, frecuencia in encontrar_palabras_mas_comunes('data/michelle_obama_speech.txt', 10):
    print(f"\"{palabra}\" aparece {frecuencia} veces")

print()

# d) Las diez palabras más frecuentes utilizadas en el discurso de Melina
print('Las diez palabras más frecuentes utilizadas en el discurso de Melina')
for palabra, frecuencia in encontrar_palabras_mas_comunes('data/melina_trump_speech.txt', 10):
    print(f"\"{palabra}\" aparece {frecuencia} veces")

print()

# c) Las diez palabras más frecuentes utilizadas en el discurso de Trump
print('Las diez palabras más frecuentes utilizadas en el discurso de Trump')
for palabra, frecuencia in encontrar_palabras_mas_comunes('data/donald_speech.txt', 10):
    print(f"\"{palabra}\" aparece {frecuencia} veces")

print()

# 4. Escribe una aplicación Python
# que verifique la similitud entre dos textos.
# Toma un archivo o una cadena como parámetro
# y evaluará la similitud entre los dos textos.
# Es posible que necesites un par de funciones:
# una para limpiar el texto (limpiar_texto),
# una para eliminar las palabras de soporte
# (eliminar_palabras_soporte)
# y finalmente para verificar la similitud
# (verificar_similitud_texto).
# La lista de palabras de paro
# se encuentra en el directorio data.


def limpiar_texto(texto):
    # Convertir todo a minúsculas
    texto = texto.lower()

    # Eliminar caracteres no alfabéticos
    texto = re.sub(r'[^a-záéíóúñ]', ' ', texto)

    # Eliminar espacios en blanco adicionales
    texto = re.sub(r'\s+', ' ', texto)

    return texto.strip()


def eliminar_palabras_soporte(texto, palabras_soporte):
    palabras = texto.split()
    palabras_filtradas = [
        palabra for palabra in palabras if palabra not in palabras_soporte]
    return ' '.join(palabras_filtradas)


def verificar_similitud_texto(texto1, texto2, palabras_soporte):
    texto1 = limpiar_texto(texto1)
    texto2 = limpiar_texto(texto2)

    texto1 = eliminar_palabras_soporte(texto1, palabras_soporte)
    texto2 = eliminar_palabras_soporte(texto2, palabras_soporte)

    palabras1 = set(texto1.split())
    palabras2 = set(texto2.split())

    similitud = len(palabras1 & palabras2) / len(palabras1 | palabras2)

    return similitud


# Leer los archivos de texto
with open('./data/michelle_obama_speech.txt', 'r') as f:
    texto1 = f.read()

with open('./data/melina_trump_speech.txt', 'r') as f:
    texto2 = f.read()

# Calcular la similitud entre los textos
similitud = verificar_similitud_texto(texto1, texto2, stop_words)

# Mostrar el resultado como un porcentaje
porcentaje_similitud = similitud * 100
print(f"La similitud entre los textos es de un {porcentaje_similitud:.2f}%\n")


# 5. Encuentra las 10 palabras más repetidas en romeo_and_juliet.txt.

for palabra, frecuencia in encontrar_palabras_mas_comunes('data/romeo_and_juliet.txt', 10):
    print(f"\"{palabra}\" aparece {frecuencia} veces")
print()

# 6. Lee el archivo CSV de hacker news y averigua:


def contar_lineas(palabra):
    archivo = 'data/hacker_news.csv'
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        contador = 0
        for linea in lineas:
            if palabra in linea:
                contador += 1
        return contador


# a) Cuántas líneas contienen python o Python

contador_python = contar_lineas('python') + contar_lineas('Python')
print(
    f"El archivo contiene {contador_python} líneas que contienen 'python' o 'Python'.")

# b) Cuántas líneas contienen JavaScript, javascript o Javascript

contador_javascript = contar_lineas(
    'JavaScript') + contar_lineas('javascript') + contar_lineas('Javascript')
print(
    f"El archivo contiene {contador_javascript} líneas que contienen 'JavaScript', 'javascript' o 'Javascript'.")

# c) Cuántas líneas contienen Java y no JavaScript

contador_java = contar_lineas('Java')
contador_javascript = contar_lineas(
    'JavaScript') + contar_lineas('Javascript')
contador_java_sin_javascript = contador_java - contador_javascript
print(
    f"El archivo contiene {contador_java_sin_javascript} líneas que contienen 'Java' pero no 'JavaScript', 'javascript' o 'Javascript'.")
