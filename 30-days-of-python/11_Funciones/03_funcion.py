"""
03_funcion.py
"""
import countries_data

# Ejercicios: Nivel 3

# 1. Escribe una función llamada is_prime
# que compruebe si un número es primo.


def is_prime(num):
    if num <= 1:
        return "No"
    elif num == 2:
        return "Sí"
    elif num % 2 == 0:
        return "No"
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return "No"
        return "Sí"


numero_primo = 19

print(f"¿El número {numero_primo} es primo? {is_prime(numero_primo)}")

# 2. Escribe una función que compruebe
# si todos los elementos de una lista son únicos.


def are_elements_unique(my_list):
    if len(my_list) == len(set(my_list)):
        return "Sí"
    else:
        return "No"


lista_elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(
    f"¿Los elementos de la lista {lista_elementos} son únicos? {are_elements_unique(lista_elementos)}")

# 3. Escribe una función que compruebe
# si todos los elementos de una lista
# son del mismo tipo de dato.


def are_elements_same_type(my_list):
    first_type = type(my_list[0])
    if not my_list:
        return "Esto no es una lista."
    elif all(isinstance(x, first_type) for x in my_list):
        return "Sí"
    else:
        return "No"


print(
    f"¿Los elementos de la lista {lista_elementos} son del mismo tipo de dato? {are_elements_same_type(lista_elementos)}")

# 4. Escribe una función que compruebe
# si una variable proporcionada
# es una variable válida en Python.


def is_valid_variable_name(variable_name):
    try:
        exec(f"{variable_name} = None")
        del locals()[variable_name]
        return "Sí"
    except:
        return "No"


print(
    f"¿La variable 'variable_name' es válida? {is_valid_variable_name('variable_name')}")

# 5. Ve a la carpeta de datos
# y accede al archivo countries-data.py.
# Crea una función llamada
# most_spoken_languages_in_the_world.
# Debe devolver las 10 o 20 lenguas
# más habladas en orden descendente.
# Crea una función llamada
# most_populated_countries.
# Debe devolver los 10 o 20 países
# más poblados en orden descendente.
# Suponiendo que los datos están almacenados
# en una lista llamada "countries_data".


# Función para obtener las lenguas
# más habladas en el mundo.

def most_spoken_languages_in_the_world():
    all_languages = []
    for country in countries_data.countries_data:
        all_languages.extend(country['languages'])

    language_count = {}

    for language in all_languages:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

    sorted_languages = sorted(language_count.items(),
                              key=lambda x: x[1],
                              reverse=True)[:10]

    language_list = [f"{i+1}. {language[0]}" for i,
                     language in enumerate(sorted_languages)]
    return "\n".join(language_list)


print(most_spoken_languages_in_the_world())

# Función para obtener los países
# más poblados en el mundo.


def most_populated_countries():
    sorted_countries = sorted(
        countries_data.countries_data, key=lambda x: x['population'], reverse=True)[:10]
    country_list = [f"{i+1}. {country['name']}" for i,
                    country in enumerate(sorted_countries)]
    return "\n".join(country_list)


print(most_populated_countries())
