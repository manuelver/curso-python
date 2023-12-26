#!/usr/bin/env python3
"""
Decoradores 
"""


def mi_decorador(funcion): # Función de orden superior

    def envoltura(): # Función anidada

        print("Esto se añade antes del función desde la envoltura")
        funcion() # Llamada a la función original
        print("Esto se añade después del función desde la envoltura")

    return envoltura


@mi_decorador
def saludo():

    print("Hola, estoy saludando dentro de la función")


saludo()

@property # Getters y Setters

