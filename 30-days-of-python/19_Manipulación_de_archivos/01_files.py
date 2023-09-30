"""
01_files.py
"""
import json


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
