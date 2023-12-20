#!/usr/bin/env python3
"""
Ejemplo de clases y objetos en Python
"""

# Clase
class Persona:

    # Método constructor (inicializador)
    def __init__(self, nombre, edad): # Persona.__init__(marcelo, "Marcelo", 25)

        # Atributos
        self.nombre = nombre
        self.edad = edad

    # Método
    def saludar(self): # Persona.saludar(marcelo)

        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"

# Instancia
marcelo = Persona("Marcelo", 25)
juan = Persona("Juan", 30)

# Imprimir método
print(marcelo.saludar())
print(juan.saludar())
