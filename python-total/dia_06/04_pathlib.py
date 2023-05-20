"""
pathlib

Las que no tienen paréntesis son funciones, no métodos

Se puede transformar a una ruta de windows importando PureWindowsPath

    PureWindowsPath(carpeta)
    
"""
from pathlib import Path

carpeta = Path(
    '/home/v/Documents/projectes/python/python_total/dia_06/prueba.txt')

print(carpeta.read_text())

# Nombre fichero
print(carpeta.name)

# sufijo. Extensión
print(carpeta.suffix)

# Nombre sin la terminación
print(carpeta.stem)

# Ver si existe el fichero con un if
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")

opcion = input("Escoger categoria: ")
if opcion.isnumeric():
    print('Es')
else:
    print("no")
