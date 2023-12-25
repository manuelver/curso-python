#!/usr/bin/env python3
"""

"""

class Caja:

    def __init__(self, *items):
        self.items = items

    def __str__(self):

        print("Se ha creado una caja con las siguientes frutas: ")

        for item in self.items:
            print(item)


caja = Caja("Manzana", "Pera", "Naranja", "Platano")
