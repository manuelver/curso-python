"""
01_conjuntos.py
"""
# Ejercicios: Nivel 1
# Conjuntos
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Encuentra la longitud del conjunto `it_companies`.
it_companies_length = len(it_companies)
print(f'La longitud de it_companies es {it_companies_length}')

# 2. Agrega 'Twitter' a `it_companies`.
it_companies.add('Twitter')

# 3. Inserta varias compañías de TI a la vez en el conjunto `it_companies`.
it_companies.update(['Intel', 'HP', 'Dell'])

# 4. Elimina una de las compañías del conjunto `it_companies`.
it_companies.remove('Dell')

# 5. ¿Cuál es la diferencia entre `remove` y `discard`?
# La diferencia es que si el elemento no existe en el conjunto,
# `remove` levanta una excepción, mientras que `discard` no hace nada.

# Ejercicios: Nivel 2

# 1. Une los conjuntos A y B.
A_union_B = A.union(B)

# 2. Encuentra la intersección entre A y B.
A_intersection_B = A.intersection(B)

# 3. ¿Es A un subconjunto de B?
A_is_subset_of_B = A.issubset(B)

# 4. ¿Son A y B conjuntos disjuntos?
A_and_B_are_disjoint = A.isdisjoint(B)

# 5. Une A con B y B con A.
A.update(B)
B.update(A)

# 6. ¿Cuál es la diferencia simétrica entre A y B?
A_symmetric_difference_B = A.symmetric_difference(B)

# 7. Elimina completamente los conjuntos.
del it_companies
del A
del B

# Ejercicios: Nivel 3

# 1. Convierte las edades a un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
age_set = set(age)
if len(age_set) > len(age):
    print('El conjunto de edades es más grande que la lista de edades')
elif len(age_set) < len(age):
    print('La lista de edades es más grande que el conjunto de edades')
else:
    print('La lista de edades y el conjunto de edades tienen la misma longitud')

# 2. Explica la diferencia entre los siguientes tipos de datos: cadena (string), lista (list), tupla (tuple) y conjunto (set).
# Una cadena (string) es una secuencia de caracteres.
# Una lista (list) es una colección ordenada y mutable de elementos.
# Una tupla (tuple) es una colección ordenada e inmutable de elementos.
# Un conjunto (set) es una colección no ordenada y mutable de elementos únicos.

# 3. Soy un profesor y me encanta inspirar y enseñar a la gente.
# ¿Cuántas palabras únicas se han utilizado en la oración?
# Utiliza los métodos `split` y `set` para obtener las palabras únicas.
sentence = 'Soy un profesor y me encanta inspirar y enseñar a la gente'
unique_words = set(sentence.split())
number_of_unique_words = len(unique_words)
print(f'Hay {number_of_unique_words} palabras únicas en la oración')
