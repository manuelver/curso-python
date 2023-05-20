"""
Directorios

Importaremos dos librerias:
Path de pathlib
os
"""
import os
from pathlib import Path

# Obtener el directorio de trabajo actual
ruta = os.getcwd()
print(ruta)

# Cambiar de directorio
ruta2 = os.chdir(
    '/home/v/Documents/projectes/python/python_total/dia_06/Europa/')
# # Leer el fichero de esa ruta
archivo = open('Consejos.txt')

print(archivo.read())

archivo.close()

# Crear rutas nuevas
os.makedirs('/home/v/Documents/projectes/python/python_total/dia_06/Africa/')

# Separar el path y el nombre del archivo

ruta3 = '/home/v/Documents/projectes/python/python_total/dia_06/Europa/Consejos.txt'

# # Nombre base del fichero o directorio de la ruta
elemento = os.path.basename(ruta3)
print(elemento)

# # ruta completa menos base
elemento2 = os.path.dirname(ruta3)
print(elemento2)

# # ruta completa en un tuple
elemento3 = os.path.split(ruta3)
print(elemento3)

# Eliminar carpeta
os.rmdir('/home/v/Documents/projectes/python/python_total/dia_06/Africa/')


# Se importa el objeto Path de la libreria pathlib para los siguientes ejercicios
# Con Path buscará en cualquier SO
carpeta = Path(
    '/home/v/Documents/projectes/python/python_total/dia_06/Europa')
archivo2 = carpeta / 'Consejos.txt'

mi_archivo = open(archivo2)

print(mi_archivo.read())

mi_archivo.close()
