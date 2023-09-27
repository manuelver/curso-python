"""
03_func_sup.py
"""
import countries_data
from collections import Counter

# Ejercicios: Nivel 3

# 1. Usa el archivo [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) y sigue las siguientes tareas:
# - Ordena los países por nombre, capital y población.

sorted_by_name = sorted(countries_data.countries,
                        key=lambda country: country['name'])

sorted_by_capital = sorted(
    countries_data.countries,
    key=lambda country: country['capital']
)

sorted_by_population = sorted(
    countries_data.countries,
    key=lambda country: country['population'],
    reverse=True
)

# Filtra los diez idiomas más hablados por ubicación

all_languages = []
for country in countries_data.countries:
    all_languages.extend(country['languages'])

# Calcula las frecuencias de cada idioma
language_counts = Counter(all_languages)

# Obtiene los diez idiomas más hablados
top_10_languages = language_counts.most_common(10)

# Filtra los diez países más poblados
top_10_population = sorted(
    countries_data.countries, key=lambda country: country['population'], reverse=True)[:10]

# Imprime los resultados
print("## Países ordenados por nombre:")
for country in sorted_by_name:
    print(country['name'])

print("\n## Países ordenados por capital:")
for country in sorted_by_capital:
    print(country['name'], "-", country['capital'])

print("\n## Países ordenados por población:")
for country in sorted_by_population:
    print(country['name'], "-", country['population'])

print("\n## Los diez idiomas más hablados por ubicación:")
for language, count in top_10_languages:
    print(language, "-", count)

print("\n## Los diez países más poblados:")
for country in top_10_population:
    print(country['name'], "-", country['population'])
