#!/usr/bin/env python3
"""
Modulos
"""

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):

    if y == 0:
        raise ValueError('[!] No se puede dividir por cero')
    else:
        return x / y

