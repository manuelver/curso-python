"""
Limpiar consola

Introducir comandos a la terminal o_O
"""
from os import system


def limpiar_consola():
    system('tree')
    system('sleep 2')
    system('clear')


nombre = input("Dime tu nombre: ")

print("Ahora te voy a mostrar directorios y ficheros durante 2 segundos")

system('sleep 2')

limpiar_consola()

print(f"¿Te quedo claro {nombre}?")
