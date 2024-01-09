#!/usr/bin/env python3
"""
Proyecto: Biblioteca
Objetivos: 
  - Crear una clase Libro que permita almacenar la información de un libro.
  - Lógica para prestar y devolver un libro.
  - Clase biblioteca infantil que herede de biblioteca y permita almacenar libros para niños.
"""


class Libro:

    def __init__(self, id, autor, titulo):

        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.esta_prestado = False

    def __str__(self):

        return f"Libro({self.id}, {self.titulo}, {self.autor})"

    def __repr__(self):

        return self.__str__()


class Biblioteca:

    def __init__(self):

        self.libros = {}  # {id: Libro(id, autor, titulo)}

    def agregar_libro(self, libro):

        if libro.id not in self.libros:

            self.libros[libro.id] = libro

        else:

            print(f"\n[!] No es posible agregar el libro con ID {libro.id}")

    def prestar_libro(self, id):

        if id in self.libros and not self.libros[id].esta_prestado:

            self.libros[id].esta_prestado = True
            print(f"\n[+] Se prestó el libro con ID {id}")

        else:

            print(f"\n[!] No es posible prestar el libro con ID {id}")

    @property
    def mostrar_libros(self):

        return [libro for libro in self.libros.values() if not libro.esta_prestado]

    @property
    def mostrar_libros_prestados(self):

        return [libro for libro in self.libros.values() if libro.esta_prestado]


class BibliotecaInfantil(Biblioteca):

    def __init__(self):

        super().__init__()
        self.libros_para_ninos = {}

    def agregar_libro(self, libro, infantil):

        super().agregar_libro(libro)
        self.libros_para_ninos[libro.id] = infantil

    def prestar_libro(self, id, es_nino):

        if id in self.libros and not self.libros[id].esta_prestado and self.libros_para_ninos[id] == es_nino:

            self.libros[id].esta_prestado = True
            print(f"\n[+] Se prestó el libro con ID {id}")

        else:

            print(f"\n[!] No es posible prestar el libro con ID {id}")

    @property
    def mostrar_libros_infantiles(self):

        return [libro for libro in self.libros.values() if self.libros_para_ninos[libro.id]]


if __name__ == '__main__':

    biblioteca = BibliotecaInfantil()

    libro1 = Libro(1, "Antoine de Saint-Exupéry", "El Principito")
    libro2 = Libro(2, "Mario Vargas Llosa", "La ciudad y los perros")
    libro3 = Libro(3, "Gabriel García Márquez", "Cien años de soledad")

    biblioteca.agregar_libro(libro1, infantil=True)
    biblioteca.agregar_libro(libro2, infantil=False)
    biblioteca.agregar_libro(libro3, infantil=False)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    biblioteca.prestar_libro(1, es_nino=True)
    biblioteca.prestar_libro(2, es_nino=False)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    print(f"\n[+] Libros prestados: {biblioteca.mostrar_libros_prestados}")

    print(f"\n[+] Libros infatiles: {biblioteca.mostrar_libros_infantiles}")
