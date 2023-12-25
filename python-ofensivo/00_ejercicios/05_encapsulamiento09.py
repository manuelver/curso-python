#!/usr/bin/env python3
"""
Métodos especiales 
"""


class Punto:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, otro):

        return Punto(self.x + otro.x, self.y + otro.y)

    def __str__(self):

        return f"Punto({self.x},{self.y})"


p1 = Punto(2, 8)
p2 = Punto(4, 9)

print(p1 + p2)  # (6, 17)
