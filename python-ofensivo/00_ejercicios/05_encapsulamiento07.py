#!/usr/bin/env python3
"""
Métodos especiales 
"""


class MiLista:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __getitem__(self, index):
        return self.data[index]

lista = MiLista()

print(lista[2])
