#!/usr/bin/env python3
"""
Métodos especiales 
"""


class Contador:

    def __init__(self, limite):

        self.limite = limite

    def __iter__(self):

        self.valor = 0

        return self

    def __next__(self):

        if self.valor < self.limite:
            self.valor += 1
            return self.valor
        else:
            raise StopIteration

c = Contador(5)

for i in c:
    print(i)
