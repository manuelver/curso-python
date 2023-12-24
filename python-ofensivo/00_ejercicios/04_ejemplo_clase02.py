#!/usr/bin/env python3
"""
Ejemplo de clases y objetos en Python
"""


class CuentaBancaria:

    # Constructor
    def __init__(self, cuenta, nombre, saldo=0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.saldo = saldo

    # Métodos
    def depositar(self, monto):

        self.saldo += monto

        return f"\n[!] Después de ingresar:\n\t[+] {self.nombre} con la cuenta \"{self.cuenta}\" tiene un saldo de {self.saldo} Euros\n"

    def retirar(self, monto):

        if monto > self.saldo:

            return f"\n[!] No se puede retirar {monto} Euros.\n[!] {self.nombre} solo tiene {self.saldo} Euros\n"

        else:

            self.saldo -= monto

            return f"\n[!] Después de retirar:\n\t[+] {self.nombre} con la cuenta \"{self.cuenta}\" tiene un saldo de {self.saldo} Euros\n"

    def consultar(self):

        return f"\n\t[+] {self.nombre} con la cuenta \"{self.cuenta}\" tiene un saldo de {self.saldo} Euros\n"


manolo = CuentaBancaria("134675640", "Manolo Vieira", 20000)

maria = CuentaBancaria("134675641", "Maria Jimenez", 10000)

print(manolo.consultar())

print(manolo.depositar(1000))

print(manolo.retirar(5000))

print(manolo.retirar(20001))

print(maria.consultar())
