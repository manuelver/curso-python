#!/usr/bin/env python3
"""
Pruebas con open de Python

w = write
r = read
a = append
b = binary
+ = read and write
"""

# Abrir fichero binario y guardarlo en otro
# imagen

with open("/home/v/Imatges/salvapantallas/peces.jpg", "rb") as f_in, open("image.png", "wb") as f_out:
    file_content = f_in.read()
    f_out.write(file_content)


# Antes
try:
    with open("test.txt", "r") as f:
        print(f.read())
except IOError:
    print("\n[!] Error: No se ha podido abrir el fichero")

# Ahora
try:
    with open("test.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\n[!] Error: No se ha podido abrir el fichero")
