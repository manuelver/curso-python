"""
random

Necesitaremos importar métodos, 
porque están en una librería llamada random

Veremos estos métodos:
randint()
uniform()
random()
choice()
shuffle()
"""
from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio_float = round(uniform(1, 10),4)
print(aleatorio_float)

aleatorio_random = random()
print(aleatorio_random)

colores = ['rosa', 'verde','negro','azul']
aleatorio_choice = choice(colores)
print(aleatorio_choice)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
