#!/usr/bin/env python3
"""
Librería os: https://docs.python.org/3/library/os.html
"""

import os

directorio_actual = os.getcwd()

print(f"\n[+] Directorio actual de trabajo: \n\t{directorio_actual}")

files = os.listdir(directorio_actual)  # Sin ruta es el directorio actual

nombre_directorio_actual = os.path.basename(directorio_actual)

print(
    f"\n[+] El directorio \"{nombre_directorio_actual}\" contiene:")

for file in files:

    print(f"\t- {file}")

if not os.path.exists("mi_directorio"):
    os.mkdir("mi_directorio")

    print(f"\n[+] Directorio \"mi_directorio\" creado:")

    files = os.listdir(directorio_actual)

else:

    print(f"\n[+] Directorio \"mi_directorio\" ya existe:")

for file in files:

    print(f"\t- {file}")

print(
    "\n[+] ¿Existe el archivo \"mi_archivo.txt\"? " +
    ("Existe" if os.path.exists("mi_archivo.txt") else "No existe") + 
    "\n"
)

value = os.getenv("HOME")

print(f"[+] Variable de entorno HOME: {value}\n")
