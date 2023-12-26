#!/usr/bin/env python3
"""
Decoradores 
"""


class Persona:

    def __init__(self, nombre, edad):

        self._nombre = nombre # Atributo protegido
        self._edad = edad # Atributo protegido

    @property # Getter
    def edad(self): # Creando Getter

        return self._edad

    @edad.setter # Setter
    def edad(self, valor): # Creando Setter

        if valor <= 0:
            raise ValueError("[!] La edad no puede ser cero o un numero negativo")

        self._edad = valor 


# manolo._edad = 36 # Setter MAL HECHO 
# NO SE DEBE ASIGNAR VALOR DIRECTAMENTE A UN ATRIBUTO PROTEGIDO

manolo = Persona("Manolo", 35)
manolo.edad = 1 # Setter
print(manolo.edad) # Getter
