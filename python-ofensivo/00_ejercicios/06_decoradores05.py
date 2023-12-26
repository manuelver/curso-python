#!/usr/bin/env python3
"""
args: argumentos posicionales
kwargs: argumentos clave
"""

import time


def cronometro(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        funcion()
        final = time.time()

        print(f"""Tiempo de ejecución de la función {funcion.__name__}: 
        {round(final - inicio, 5)} segundos""")

        if args:
            print(f"Argumentos: {args}")
        
        if kwargs:
            print(f"Argumentos clave: {kwargs}")

    return envoltura


@cronometro
def pausa_corta(*args, **kwargs):
    time.sleep(1)


@cronometro
def pausa_larga(*args, **kwargs):
    time.sleep(2)


pausa_corta(2, 3, 4, 5, 6, 7, nombre="Juan", edad=23)
pausa_larga()
