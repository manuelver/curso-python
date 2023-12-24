#!/usr/bin/env python3
"""
Clases subclases y herencia
"""


class Automovil:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        
        return f"Marca: {self.marca}\nModelo: {self.modelo}\n"


class Coche(Automovil):

    def describir(self):
        return f"[+] Coche:\n   [+] Marca: {self.marca}\n   [+] Modelo: {self.modelo}\n"

class Moto(Automovil):

    def describir(self):
        return f"[+] Moto:\n   [+] Marca: {self.marca}\n   [+] Modelo: {self.modelo}\n"

def describir_vehiculo(vehiculo): # Polimorfismo

    print(vehiculo.describir())

coche = Coche("Mazda", "MX5")
moto = Moto("Honda", "CBR")

describir_vehiculo(coche)
describir_vehiculo(moto)
