#!/usr/bin/env python3
"""
Atributo privado
"""


class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0  # Atributo privado

    def conducir(self, km):

        if km >= 0:
            self.__kilometraje += km
        else:
            print("\n[!] Los kilometros deben ser mayores de 0\n")

    def mostrar_kilometraje(self):
        return self.__kilometraje


coche = Coche("Toyota", "Corolla")
coche.conducir(150)

# Esto no se hace, te matan los desarrolladores
print(coche._Coche__kilometraje)

print(coche.mostrar_kilometraje())  # El convenio especifica que se haga así
