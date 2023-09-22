"""
02_bucles.py
"""

# Ejercicios: Nivel 2

# 1. Utiliza un bucle for para iterar de 0 a 100
# e imprime la suma de todos los números.
suma_total = 0
for i in range(101):
    suma_total += i
print(f'La suma de todos los números es {suma_total}.')

# 2. Utiliza un bucle for para iterar de 0 a 100
# e imprime la suma de todos los números pares
# y la suma de todos los números impares.
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print(
    f'La suma de todos los números pares es {suma_pares}. \nLa suma de todos los números impares es {suma_impares}.')
