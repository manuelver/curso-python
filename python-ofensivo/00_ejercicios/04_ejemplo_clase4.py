#!/usr/bin/env python3
"""
Ejemplo de clases y objetos en Python
"""


class Libro:

    bestseller_value = 5000  # Variable de clase
    IVA = 0.21  # Variable de clase

    def __init__(self, titulo, autor, precio, ventas=7000):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.ventas = ventas

    def __str__(self):
        return "\n[*] {} escrito por {} tiene un precio de {} euros y se ha vendido {} veces.\n".format(
            self.titulo,
            self.autor,
            self.precio,
            self.ventas
        )

    @staticmethod  # Decorador
    def es_best_seller(ventas):
        if ventas > Libro.bestseller_value:  # Las variables de clase se llaman con el nombre de la clase
            return f"[*] Lo ha petado.\n"
        else:
            return f"[*] No lo ha petado.\n"

    @classmethod # Decorador
    def precio_con_iva(cls, precio):

        precio_con_iva = precio * (1 + cls.IVA) # Las variables se llama con el nombre de la clase

        return round(precio_con_iva, 2)


class LibroDigital(Libro):

    IVA = 0.10


# Instancia
mi_libro = Libro("El Quijote", "Miguel de Cervantes", 18.7)
mi_libro_digital = LibroDigital("El Quijote", "Miguel de Cervantes", 18.7)

print(
    mi_libro
)

# Con el decorador no tienes por qué instanciar el objeto, puedes hacerlo a la clase.
print(
    Libro.es_best_seller(mi_libro.ventas)
)

print(
    f"[*] El precio con IVA es de {Libro.precio_con_iva(mi_libro.precio)} euros.\n"
)

print(
    f"[*] El precio con IVA del libro digital es de {LibroDigital.precio_con_iva(mi_libro_digital.precio)} euros.\n"
)
