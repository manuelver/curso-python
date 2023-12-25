#!/usr/bin/env python3
"""
Ejemplo de clases y objetos en Python
"""

class rectangulo:

    def __init__(self, base, altura):

        self.base = base

        self.altura = altura

    @property
    def area(self):

        return self.base * self.altura

# Propiedad especiales de la clase
    def __str__(self):

        return f"\n[+]Propiedades del rectangulo:\n\t[+] Base: {self.base}\n\t[+] Altura: {self.altura}\n"

    def __eq__(self, otro):

        return self.base == otro.base and self.altura == otro.altura


rect1 = rectangulo(3, 4)
rect2 = rectangulo(3, 4)

print(rect1)
print(f"[+] El area del rectangulo es: {rect1.area}\n")
print(f"[+] ¿Son iguales rect1 y rect2? --> {rect1 == rect2}\n")
