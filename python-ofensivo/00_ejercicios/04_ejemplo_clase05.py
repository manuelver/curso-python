#!/usr/bin/env python3
"""
Ejemplo de clases y objetos en Python
"""


class Estudiantes:

    estudiantes = []

    def __init__(self, nombre, edad, sexo):

        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_de_edad(edad):

        return edad >= 18

    @classmethod
    def crear_estudiante(cls, nombre, edad, sexo):

        if cls.es_mayor_de_edad(edad):

            return cls(nombre, edad, sexo)
        else:
            print(
                f"[!] Error: El estudiante {nombre} tienen {edad}, no es mayor de edad")

    @staticmethod
    def mostrar_estudiantes():

        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(
                f"\n[+] Estudiante número {i+1}:\n\t[+] Nombre: {estudiante.nombre}\n\t[+] Edad: {estudiante.edad}\n\t[+] Sexo: {estudiante.sexo}")


Estudiantes.crear_estudiante("Juan", 18, "M")
Estudiantes.crear_estudiante("Maria", 19, "F")
Estudiantes.crear_estudiante("Pedro", 12, "M")
Estudiantes.crear_estudiante("Luisa", 29, "F")

print("\n[i] Listado de estudiantes:\n")

Estudiantes.mostrar_estudiantes()
