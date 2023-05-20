"""
Enumerador
"""

lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

# Con el enumerador es mucho más elegante
for item in enumerate(lista):
    print(item)

# La anterior devuelve un tuple,
# podemos separarla con una variable
for indice,item in enumerate(lista):
    print(indice, item)

# Junto a range podemos extraer un indice de la iteración
for indice,item in enumerate(range(50,55)):
    print(indice, item)

# Se puede utilizar para transformar una lista en un tuple

mis_tuples = list(enumerate(lista))
print(mis_tuples)
# Podemos acceder a un valor concreto a través de los indices
print(mis_tuples[1][1])
