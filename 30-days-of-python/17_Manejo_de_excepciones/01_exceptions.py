"""
01_exceptions.py
"""


# 1. Desempaca los cinco primeros países
# y almacénalos en una variable
# llamada 'nordic_countries',
# almacena 'Estonia' y 'Russia'
# en variables 'es' y 'ru'
# respectivamente.

names = [
    'Finland',
    'Sweden',
    'Norway',
    'Denmark',
    'Iceland',
    'Estonia',
    'Russia'
]

nordic_countries = names[:5]

es, ru = names[-2:]

for country in nordic_countries:
    print(country)

print(f"\n{es}\n\n{ru}\n ")
print("\U0001F604")
