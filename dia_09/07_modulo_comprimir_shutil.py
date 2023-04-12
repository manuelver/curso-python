"""
Módulos comprimir y descomprimir

shutil - Nos permite comprimir 
todos los archivos y directorios de una carpeta

"""

import shutil

carpeta_origen = 'carpeta_superior'

archivo_destino = 'todo_comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)
