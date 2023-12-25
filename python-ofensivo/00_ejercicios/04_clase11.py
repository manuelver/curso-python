#!/usr/bin/env python3
"""
Sobeescribir el constructor de una clase con super
"""


class A:

    def __init__(self, x):
        self.x = x

        print(f"Valor de x: {self.x}")

class B(A):

    def __init__(self, x, y):
        self.y = y
        # Forzar que se ejecute el constructor de A
        super().__init__(x)
        print(f"Valor de y: {self.y}")

b = B(2, 10)

