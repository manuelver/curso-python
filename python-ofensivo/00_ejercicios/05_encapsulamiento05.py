#!/usr/bin/env python3
"""
Métodos especiales 
"""


class Caja:

    def __init__(self, *items):
        self.items = items

    def mostrar_items(self):

        print("Se ha creado una caja con las siguientes frutas: ")

        for item in self.items:
            print(item)

    def __len__(self):

        return len(self.items)


caja = Caja("Manzana", "Pera", "Naranja", "Platano", "Melon")

caja.mostrar_items()

print("La caja tiene {} frutas".format(len(caja)))
