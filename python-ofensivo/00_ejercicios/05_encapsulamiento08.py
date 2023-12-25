#!/usr/bin/env python3
"""
Métodos especiales 
"""


class Saludo:

    def __init__(self, saludo):

        self.saludo = saludo

    def __call__(self, nombre):

        return f"{self.saludo} {nombre}!"


hola = Saludo("¡Hola")

print(hola("Luis"))

print(hola("Juan"))
