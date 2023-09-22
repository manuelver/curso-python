"""
01_bucles.py
"""
# Ejercicios: Nivel 1

# 1. Itera de 0 a 10 utilizando un bucle for,
# haz lo mismo utilizando un bucle while.
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Itera de 10 a 0 utilizando un bucle for,
#  haz lo mismo utilizando un bucle while.
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Escribe un bucle que haga siete llamadas a `print()`,
# de modo que obtengamos el siguiente triángulo en la salida:
for i in range(1, 8):
    print('#' * i)

# 4. Utiliza bucles anidados para crear lo siguiente:
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# 5. Imprime el siguiente patrón:
for i in range(11):
    print(f'{i} x {i} = {i*i}')

# 6. Itera a través de la lista
# `['Python', 'Numpy', 'Pandas', 'Django', 'Flask']`
# utilizando un bucle for e imprime los elementos.
for elemento in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(elemento)

# 7. Utiliza un bucle for para iterar de 0 a 100
# e imprime solo los números pares.
for i in range(0, 101, 2):
    print(i)

# 8. Utiliza un bucle for para iterar de 0 a 100
# e imprime solo los números impares.
for i in range(1, 101, 2):
    print(i)
