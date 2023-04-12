"""
Módulos os y shutil

También método send2trash

"""

import os
import shutil
import send2trash

# Mostrar el directorio actual
print(os.getcwd())

# Vamos a abrir un archivo. Como no existe se creará.
# Usamos la 'w' para escribir en él
archivo = open('curso.txt', 'w')

archivo.write('texto de prueba')

archivo.close()


print()
# Mostrar archivos de la ubicación actual
print(os.listdir())


print()
# Mover archivos con shutil
# Movemos curso al día_08
# Se puede con rutas relativas o absolutas
shutil.move('curso.txt', '../dia_08')

# Varios métodos para eliminar ficheros
# unlink - Elimina los ficheros de la ruta que digas
#     os.unlink(path)

# rmdir - Elimina directorios de la ruta que digas
#     os.rmdir(path)

# rmt - Eliminar todo CUIDAO Elimina todo y es irreversible
#     shutil.rmt

# Pongo una pausa para ver como
# se crea y elimina el fichero
sleep = 'sleep 3'
os.system(sleep)


# Para eliminar enviando a la papelera
# mejor con el método send2trash
send2trash.send2trash('../dia_08/curso.txt')


# walk - Recorrer carpetas

# Si lo imprimimos directamente
# nos dice que es un generator

print(os.walk('../..'))

# así que la info la proporciona tal como se le pide
print()
# Creamos una variable con la ruta
ruta = '../dia_08'

# Hay que tener en cuenta que guarda tuplas con
# - carpetas
# - subcarpetas
# - ficheros
# Vamos a extraerlo con un iterador
for carpeta, subcarpeta, fichero in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')

    print('Los archivos son: ')
    for arch in fichero:
        # En los ficheros le vamos a poner un filtro
        # para que imprima solo lo que nos interesa
        if arch.startswith('0'):
            print(f'\t{arch}')
    print()
