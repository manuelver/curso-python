#!/usr/bin/env python3
"""
Ejemplo de métodos especiales
"""


class Libro:

    def __init__(self, autor, titulo):

        self.titulo = titulo
        self.autor = autor

    def __str__(self):

        return f"El libro '{self.titulo}' fue escrito por {self.autor}"

    def __eq__(self, otro):

        return self.titulo == otro.titulo and self.autor == otro.autor


libro_uno = Libro("Jose Saramago", "Ensayo sobre la ceguera")
libro_dos = Libro("Jose Saramago", "Ensayo sobre la vista")

print(libro_uno)
print(libro_dos)

print(f"¿Son iguales ambos libros? --> {libro_uno == libro_dos}")
