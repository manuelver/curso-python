"""
Se puede ver con dir() las funciones que tiene un módulo

Con builtin_module_names se puede ver los módulos que vienen por defecto en 
python

Por supuesto, se pueden ver todos los módulos descargados con pip con:
pip freeze

Se puede ver la ubicación de un módulo externo con __file__ 

También se puede buscar la ubicación de los módulos con el path de python con 
sys.path

"""

import math
import sys
import hashlib


print(dir(math))
print()
print(sys.builtin_module_names)
print()
print(hashlib.__file__)
print()
print(sys.path)
print()

# Ejemplo de uso hashlib
print(hashlib.md5(b'Hello World').hexdigest())
