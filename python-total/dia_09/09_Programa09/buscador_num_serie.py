"""
Programa día 9 - Buscador de números de serie

- Recorrer todos los archivos 
y subcarpetas de directorio raiz Mi_Gran_Directorio. método walk() de os.
- Buscar string qye coincida con un patrón de número de serie
- Como mucho un número de serie por fichero.
módulo os para abrir e iterear por el directorio
expresiones regulares para encontrar el formato de número de serie correcto.
Formato:
[N] + [tres carateres de texto] + [-] + [5 números]
Ejemplo: Nryu-12365
Presentación de resultados:
----------------------------------------------------
Fecha de búsqueda: [fecha de hoy - formato dd/mm/aa]

ARCHIVO		NRO. SERIE
-------		----------
texto1.txt	Nter-15496
texto25.txt	Ngba-85235

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------

- La 'Duración de búsqueda' debe estar redondeada hacia arriba

"""

from datetime import date
import os
from pathlib import Path
import re
import time
import math


def fecha_hoy():
    """
    Devuelve la fecha actual
    """

    hoy = date.today().strftime('%d/%m/%Y')
    fecha = f'\nFecha de búsqueda: {hoy}'

    return fecha


def abrir_fichero(file_path):
    """
    Recoge un path de un fichero 
    y devuelve el contenido del fichero
    """

    with open(file_path, encoding="utf-8") as file:
        contenido = file.read()

    return contenido


def busqueda_serie():
    """
    Buscador
    """

    patron = r'N\D{3}-\d{5}'
    ruta = './Mi_Gran_Directorio'
    lista_filas = []

    for root, sub, fichero in os.walk(ruta):
        if fichero:
            for arch in fichero:
                sub.clear()
                texto = abrir_fichero(Path(root, arch))
                busqueda = re.findall(patron, texto)
                if re.findall(patron, texto):
                    fila = f'{arch}\t| {busqueda[0]}\t| {root}'
                    lista_filas.append(fila)

    lista_filas.sort()
    return lista_filas


def tiempo_ejecucion():
    """
    Ejecuta la búsqueda y devuelve 
    - La busqueda
    - El contador
    - El tiempo de ejecución
    """

    inicio = time.time()
    busqueda_serie()
    final = time.time()
    tiempo_total = math.ceil(final - inicio)

    return tiempo_total


print(f'\n{fecha_hoy()}')

print("""
NOMBRE ARCHIVO\t| NRO. SERIE\t| UBICACIÓN DEL FICHERO
--------------\t| ----------\t| ---------------------""")
for f in busqueda_serie():
    print(f)

print(f'\nNúmeros encontrados: {len(busqueda_serie())}')
print(f'Duración de la búsqueda: {tiempo_ejecucion()} seg.\n')
