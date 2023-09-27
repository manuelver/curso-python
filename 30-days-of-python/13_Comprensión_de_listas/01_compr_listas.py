"""
01_compr_listas.py
"""


# Ejercicios: Nivel 1

# 1. Filtra solo los números negativos y cero
# en la lista usando una comprensión de lista.

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]

print(filtered_numbers)

print("")

# 2. Aplana la siguiente lista de listas de listas
# a una lista unidimensional:

list_of_lists = [
    [[1, 2, 3]],
    [[4, 5, 6]],
    [[7, 8, 9]]
]

flattened_list = [
    num for sublist in list_of_lists for subsublist in sublist for num in subsublist]

print(flattened_list)

print("")

# 3. Usando una comprensión de lista,
# crea la siguiente lista de tuplas:

tuples_list = [
    (i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)
]

for tpl in tuples_list:
    print(str(tpl).replace(", ", ","))

print("")

# 4. Aplana la siguiente lista
# a una nueva lista:

countries = [
    [
        ('Finland', 'Helsinki')
    ],
    [
        ('Sweden', 'Stockholm')
    ],
    [
        ('Norway', 'Oslo')
    ]
]

flattened_countries = [
    [
        country.upper(),
        country[:3].upper(),
        city.upper()
    ]
    for sublist in countries for country,
    city in sublist
]

for sublist in flattened_countries:
    print(sublist)

print("")

# 5. Cambia la siguiente lista
# a una lista de diccionarios:

countries = [
    [('Finland', 'Helsinki')], [
        ('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

dict_list = [
    {'country': country, 'city': city}
    for sublist in countries for country,
    city in sublist
]

for dct in dict_list:
    print(dct)

print("")

# 6. Cambia la siguiente lista de listas
# a una lista de cadenas concatenadas:

names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]

concatenated_names = [' '.join(name) for sublist in names for name in sublist]

print(concatenated_names)

print("")

# 7. Escribe una función lambda
# que pueda resolver una pendiente
# o una ordenada al origen de funciones lineales.

# La función lambda toma dos argumentos: x y m, donde x es la variable independiente y m es la pendiente.
# La función devuelve la ordenada al origen de la función lineal.


def linear_function(x, m):
    return -m * x


x = imn
m = 2
result = linear_function(x, m)

print(
    f"Para x = {x} y m = {m}, el resultado de la función lineal es {result}.")
