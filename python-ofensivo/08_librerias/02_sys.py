#!/usr/bin/env python3
"""
Documentación Librería sys: https://docs.python.org/3/library/sys.html 

Para ver los argumentos ejecutar:
python3 pruebas.py arg1 arg2 arg3
"""

import sys

print(f"\n[+] Nombre del script: {sys.argv[0]}")
print(f"\n[+] Número de argumentos: {len(sys.argv)}")
print(f"\n[+] Argumentos: {', '.join(arg for arg in sys.argv[1:])}")

print(f"\n[+] Path de librerías Python:")

for path in sys.path:
    print(f"- {path}")

print(f"\n[+] Saliendo con un código de estado 1 (no exitoso)")
sys.exit(1)
