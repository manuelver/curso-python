#!/usr/bin/env python3
"""
Sobeescribir el constructor de una clase con super desde una subclase
"""


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"


class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def saludo(self):

        return f"{super().saludo()}, cobro {self.sueldo} euros brutos al año."


persona = Empleado("Juan", 28, 35000)

print(persona.saludo())

