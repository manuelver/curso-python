"""
Módulo collections

Counter - Es una especia de diccionario 
que cuentas elementos de una lista, tupla o string

DefaultDict - Da valores por defecto

NamedTuple - Tupla con nombres. 
Sirve para tener nombres además de índices

deque - contenedor similar a una lista con appends 
y pops rápidos en ambos extremos

"""

from collections import Counter, defaultdict, namedtuple, deque


# Counter

numeros = [8, 6, 9, 5, 4, 5, 5, 5, 8, 7, 4, 3, 5, 4, 4]

print(Counter(numeros))
print(Counter('mississippi'))

print()
# Se puede utilizar módulos de Counter
serie = Counter([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4])
# En orden del más común a menos
print(serie.most_common())
# Podemos meter Counter en una lista
print(list(serie))


print()
# DefaultDict

mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'

# Cuando se llama a un valor que no existe
# defaultdict lo añadirá con el valor por defecto
print(mi_dic['cuatro'])

print(mi_dic)


print()
# NamedTuple

# Creamos una clase y con NamedTuple nombramos
# a los elementos de la tupla
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

# Damos valores
ariel = Persona('Ariel', 1.76, 67)

# y podemos imprimir por el nombre dado
print(ariel.altura)
print(ariel.peso)

# Sin perder la manera clásica de llamarle
# por el índice
print(ariel[0])


# deque
lista_ciudades = deque(
    ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.appendleft('Badajoz')

print(lista_ciudades)
