"""
01_func_sup.py
"""


# Ejercicios: Nivel 1


# 1. Explica la diferencia entre map, filter y reduce.

# map, filter y reduce son funciones integradas en Python
# que se utilizan para procesar y transformar datos.

# map toma una función y una secuencia
# y aplica la función a cada elemento de la secuencia,
# devolviendo una nueva secuencia con los resultados.

# filter toma una función y una secuencia
# y devuelve una nueva secuencia
# que contiene solo los elementos de la secuencia original
# para los cuales la función devuelve True.

# reduce toma una función y una secuencia
# y aplica la función a los elementos de la secuencia
# de izquierda a derecha, reduciendo la secuencia a un solo valor.


# 2. Explica la diferencia entre función
# de orden superior, cierre y decorador.

# Una función de orden superior es una función
# que toma una o más funciones como argumentos
# y/o devuelve una función como resultado.

# Un cierre es una función
# que recuerda el estado
# de su entorno léxico cuando se define
# y puede acceder a ese estado
# incluso cuando se llama en un entorno diferente.

# Un decorador es una función
# que toma otra función
# y extiende o modifica su comportamiento
# sin cambiar su código fuente.


# 3. Define una función de llamada antes de map, filter o reduce,
# mira los ejemplos.

# map
from functools import reduce


def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))

print(doubled_numbers)


# filter
def is_even(x):
    return x % 2 == 0


even_numbers = list(filter(is_even, numbers))

print(even_numbers)

# reduce


def add(x, y):
    return x + y


sum = reduce(add, numbers)

print(sum)


# 4. Usa un bucle for para imprimir cada país
# en la lista de países.

countries = ["Spain", "France", "Germany", "Italy"]

for country in countries:
    print(country)

# 5. Usa un bucle for para imprimir cada nombre
# en la lista de nombres.

names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    print(name)

# 6. Usa un bucle for para imprimir cada número
# en la lista de números.

for number in numbers:
    print(number)
