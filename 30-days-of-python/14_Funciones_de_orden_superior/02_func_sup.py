"""
02_func_sup.py
"""
from functools import reduce
import countries
# Ejercicios: Nivel 2


# 1. Usa map para crear una nueva lista
# cambiando cada país a mayúsculas
# en la lista de países.


upper_countries = list(map(str.upper, countries.countries))

print(upper_countries)

print()

# 2. Usa map para crear una nueva lista
# cambiando cada número por su cuadrado
# en la lista de números.

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)

print()

# 3. Usa map para cambiar
# cada nombre a mayúsculas
# en la lista de nombres.

names = ["Alice", "Bob", "Charlie", "David"]
upper_names = list(map(str.upper, names))

print(upper_names)

print()

# 4. Usa filter para filtrar
# los países que contengan 'land'.

land_countries = list(filter(lambda x: "land" in x, countries.countries))

print(land_countries)

print()

# 5. Usa filter para filtrar los países
# que tengan exactamente seis caracteres.

six_letter_countries = list(filter(lambda x: len(x) == 6, countries.countries))

print(six_letter_countries)

print()

# 6. Usa filter para filtrar los países
# que contengan seis letras
# o más en la lista de países.

long_countries = list(filter(lambda x: len(x) >= 6, countries.countries))

print(long_countries)

print()

# 7. Usa filter para filtrar los países
# que comiencen con 'E'.

e_countries = list(filter(lambda x: x.startswith("E"), countries.countries))

print(e_countries)

print()

# 8. Encadena dos o más iteradores de lista
# (por ejemplo,
# arr.map(callback).filter(callback).reduce(callback)).

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(result)

print()

# 9. Declara una función llamada get_string_lists
# que tome una lista como parámetro
# y luego devuelva una lista que contenga
# solo elementos de tipo cadena.


def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))


mixed_list = [1, "hello", 2, "world", 3]
string_list = get_string_lists(mixed_list)

print(string_list)

print()

# 10. Usa reduce para sumar todos los números
# en la lista de números.


numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)

print(sum)

print()

# 11. Usa reduce para concatenar todos los países
# y producir la siguiente oración:
# Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.

sentence = reduce(lambda x, y: x + ", " + y, countries.countries)

print(sentence + " son países del norte de Europa.")

print()

# 12. Declara una función llamada categorize_countries
# que devuelva una lista de países
# con algún patrón común de countries.py


def categorize_countries():
    patterns = ["land", "ia", "island", "stan"]
    categorized_countries = []
    for pattern in patterns:
        matching_countries = list(
            filter(lambda x: pattern in x.lower(), countries.countries))
        categorized_countries.append(matching_countries)

    return categorized_countries


print(categorize_countries())

print()

# 13. Crea una función que devuelva un diccionario,
# donde las claves sean las letras iniciales de los países
# y los valores sean la cantidad de nombres de países
# que comienzan con esa letra.


def count_countries_by_initial():
    counts = {}
    for country in countries.countries:
        initial = country[0]
        if initial in counts:
            counts[initial] += 1
        else:
            counts[initial] = 1
    return counts


print(count_countries_by_initial())

print()

# 14. Declara una función llamada get_first_ten_countries
# que devuelva una lista de los primeros diez países
# de la lista de países.


def get_first_ten_countries():

    return countries.countries[:10]


print(get_first_ten_countries())

print()

# 15. Declara una función llamada get_last_ten_countries
# que devuelva los últimos diez países
# en la lista de países.


def get_last_ten_countries():

    return countries.countries[-10:]


print(get_last_ten_countries())

print()
