#!/usr/bin/env python3
"""
Pruebas con open de Python

w = write
r = read
a = append
b = binary
+ = read and write
"""

f = open('example.txt', 'w')  # Cuidado! Que borra lo que haya en el fichero
f.write('¡Hola mundo!\n')
f.write('k ase')
f.close()

f = open('example.txt', 'a')
f.write('\n¡Hasta luego mundo!\n')
f.close()

# Lo más óptimo es usar with
# De esta manera se cierra automáticamente el fichero

with open('example.txt', 'r') as f:
    file_content = f.read()

print(file_content)


# Se puede leer línea a línea
# end='' para que no haga un salto de línea
# line.strip() para quitar los espacios en blanco

with open('/etc/hosts', 'r') as f:
    for line in f:
        print(line, end='')

# Se puede crear una lista con el contenido del fichero

mi_lista = [
    "Primera línea\n",
    "Segunda línea\n",
    "Tercera línea\n",
    "Cuarta línea\n"
]

with open('example.txt', 'w') as f:
    f.writelines(mi_lista)

with open('example.txt', 'r') as f:
    for line in f:
        print(line, end='')

# with open("/etc/passwd", "r") as f:
#     for line in f.readlines():  # Abre todo el fichero y lo mete en una lista
#         print(line, end='')

print()

# with open("/etc/passwd", "r") as f:
#     for line in f.readline(): # Abre solo la primera línea
#         print(line, end='')


with open("example.txt", "w") as f:
    print("Primera línea", file=f) # También se puede guardar así

with open("example.txt", "r") as f:
    for line in f:
        print(line, end='')
