#!/usr/bin/env python3
"""
*args: argumentos posicionales

**kwargs: argumentos nombrados
"""

# EJEMPLO DE *args


def suma(*args):

    return sum(args)


# EJEMPLO DE **kwargs

def presentacion(**kwargs):

    print("[+] Mis datos:")
    for key, value in kwargs.items():

        print(f"\t- {key}: {value}")


presentacion(
    nombre="Juan",
    edad=20,
    ciudad="Medellín",
    profesion="Lammer"
)
