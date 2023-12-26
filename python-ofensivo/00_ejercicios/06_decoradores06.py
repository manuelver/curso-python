#!/usr/bin/env python3
"""
Decoradores
"""

import math

PI = math.pi


class Circunferencia:

    def __init__(self, radio):
        self._radio = radio  # _radio es un atributo protegido

    @property  # Getter
    def radio(self):

        return self._radio

    @property
    def diametro(self):

        return self._radio * 2

    @property
    def area(self):

        return round(self._radio**2 * PI, 2)

    @radio.setter  # Setter
    def radio(self, radio):

        if radio >= 0:
            self._radio = radio
        else:
            raise ValueError("El radio no puede ser negativo")


c = Circunferencia(5)

print(f"[+] El radio es de {c.radio} cm")
print(f"[+] El diametro es de {c.diametro} cm")
print(f"[+] El area es de {c.area} cm^2")

print()

c.radio = 10
print(f"[+] El radio es de {c.radio} cm")
print(f"[+] El diametro es de {c.diametro} cm")
print(f"[+] El area es de {c.area} cm^2")
