"""
Módulos comprimir y descomprimir

zipfile

"""

import zipfile


zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

zip_abierto.extractall()
