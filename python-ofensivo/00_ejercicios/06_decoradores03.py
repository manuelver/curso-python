#!/usr/bin/env python3
"""
Decoradores 
"""

import time

def cronometro(funcion):
    def envoltura(n): # Si la función recibe parámetros se deben pasar a la envoltura
        inicio = time.time()
        funcion(n) # Si la función recibe parámetros se deben pasar a la función
        final = time.time()

        print(f"""Tiempo de ejecución de la función {funcion.__name__}: 
        {round(final - inicio, 5)} segundos""")

    return envoltura

@cronometro
def pausa_corta(num):
    time.sleep(num)

@cronometro
def pausa_larga(num):
    time.sleep(num)


pausa_corta(2)
pausa_larga(3)
