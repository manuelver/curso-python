#!/usr/bin/env python3
"""
Clases con herencia y polimorfismo
"""


class Animal:

    def __init__(self, nombre):

        self.nombre = nombre


    def hablar(self):

        # Definimos una salida de errror
        raise NotImplementedError("La subclase debe implementar este método abstracto")

class Gato(Animal):

    def hablar(self):

        return f"¡miau!"

class Perro(Animal):

    def hablar(self):

        return f"¡guau!"


def hacer_hablar(objeto):

    print(f"{objeto.nombre} dice {objeto.hablar()}")


gato = Gato("Lucas")
perro = Perro("Firulais")
vaca = Animal("Lola")

print(gato.hablar())
print(perro.hablar())
# print(vaca.hablar()) # Provocar error

hacer_hablar(gato)
hacer_hablar(perro)

