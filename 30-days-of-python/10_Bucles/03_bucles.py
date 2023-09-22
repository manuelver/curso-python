"""
03_bucles.py
"""

# Ejercicios: Nivel 3

import os
import sys
import json
import countries

# 1. Ve a la carpeta de datos y utiliza el archivo countries.py.
# Recorre los países y extrae todos los países
# que contienen la palabra "land".
sys.path.append(os.path.join(os.getcwd(), 'data'))

for country in countries.countries:
    if 'land' in country:
        print(country)

# 2. Esta es una lista de frutas: `['banana', 'naranja', 'mango', 'limón']`.
# Invierte el orden utilizando un bucle.
frutas = ['banana', 'naranja', 'mango', 'limón']

for i in range(len(frutas) - 1, -1, -1):
    print(frutas[i])

# 3. Ve a la carpeta de datos y utiliza el archivo countries_data.py.
with open(os.path.join('data', 'countries_data.json')) as f:
    countries_data = json.load(f)

# ¿Cuál es el número total de idiomas en los datos?
idiomas = set()
for country in countries_data:
    for language in country['languages']:
        idiomas.add(language)

print(f'El número total de idiomas en los datos es {len(idiomas)}.')

# Encuentra los diez idiomas más hablados en los datos.
idiomas_hablados = {}
for country in countries_data:
    for language in country['languages']:
        if language in idiomas_hablados:
            idiomas_hablados[language] += country['population']
        else:
            idiomas_hablados[language] = country['population']

idiomas_top_10 = sorted(idiomas_hablados.items(),
                        key=lambda x: x[1], reverse=True)[:10]
print('Los diez idiomas más hablados en los datos son:')
for idioma, poblacion in idiomas_top_10:
    print(f'{idioma}: {poblacion}')

# Encuentra los 10 países más poblados del mundo.
paises_top_10 = sorted(
    countries_data, key=lambda x: x['population'], reverse=True)[:10]
print('Los diez países más poblados del mundo son:')
for pais in paises_top_10:
    print(f"{pais['name']}: {pais['population']} habitantes.")
