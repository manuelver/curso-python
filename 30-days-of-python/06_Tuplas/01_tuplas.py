"""
01_tuplas.py
"""

# 1. Crea una tupla vacía.
empty_tuple = ()

# 2. Crea una tupla que contenga los nombres de tus hermanas y hermanos (hermanos imaginarios están bien).
hermanos_tuple = ('Mario', 'Maria', 'Juan', 'Juana')

# 3. Une las tuplas de hermanos y hermanas y asígnalo a `siblings`.
siblings = hermanos_tuple

# 4. ¿Cuántos hermanos tienes?
numero_hermanos = len(siblings)
print(f'Tienes {numero_hermanos} hermanos')

# 5. Modifica la tupla `siblings` y agrega el nombre de tu padre y madre, asígnalo a `family_members`.
family_members = siblings + ('padre', 'madre')

# 6. Desempaqueta hermanos y padres de `family_members`.
hermano1, hermana1, hermano2, hermana2, padre, madre = family_members

# 7. Crea tuplas de frutas, verduras y productos de origen animal. Une las tres tuplas y asígnalo a una variable llamada `food_stuff_tp`.
frutas = ('manzana', 'banana', 'naranja')
verduras = ('lechuga', 'tomate', 'cebolla')
productos_animal = ('miel', 'huevos', 'caviar')
food_stuff_tp = frutas + verduras + productos_animal

# 8. Cambia la tupla `food_stuff_tp` a una lista llamada `food_stuff_lt`.
food_stuff_lt = list(food_stuff_tp)

# 9. Corta el elemento o elementos del medio de la tupla `food_stuff_tp` o la lista `food_stuff_lt`.
if len(food_stuff_lt) % 2 == 0:
    food_stuff_lt = food_stuff_lt[:len(
        food_stuff_lt) // 2 - 1] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
else:
    food_stuff_lt = food_stuff_lt[:len(
        food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]

# 10. Corta los tres primeros elementos y los tres últimos elementos de la lista `food_stuff_lt`.
food_stuff_lt = food_stuff_lt[3:-3]

# 11. Elimina completamente la tupla `food_staff_tp`.
del food_stuff_tp

# 12. Verifica si un elemento existe en la tupla:
nordic_countries = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')

# - Verifica si 'Estonia' es un país nórdico.
if 'Estonia' in nordic_countries:
    print('Estonia es un país nórdico')
else:
    print('Estonia no es un país nórdico')

# - Verifica si 'Iceland' es un país nórdico.
if 'Iceland' in nordic_countries:
    print('Iceland es un país nórdico')
else:
    print('Iceland no es un país nórdico')
