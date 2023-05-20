"""
Tuplas

Es exactamente lo mismo que una lista 
pero no permite modificación alguna
"""

numeros = (1, 2, 3)

# Se puede concatenar tuplas pero creando una nueva

mas_numeros = numeros + (4, 5, 6, 7)

print(mas_numeros)

# Se puede transformar una lista en una tupla
punto = tuple([1, 2])

"""
Sets

Es una colección o un conjunto. 
No se puede repetir ni está ordenada
No tienen indice
"""
primer_set = {1, 1, 1, 2, 3, 3, 4, 4, 4, 5}

print(primer_set)

primer_set.add(6)
primer_set.remove(1)

print(primer_set)

# transformar lista en set
segundo = [4, 5, 6, 7, 8, 9]
segundo = set(segundo)

print(segundo, type(segundo))

# Operadores

# # Operador unión |
# # devolver todo junto eliminando repetidos
print(primer_set | segundo)

# # Operador intersección
# # devolverá los elementos
# # que se encuentren en los dos sets &
print(primer_set & segundo)

# # Operador diferencia
# # Mostrar los elementos de la izquierda
# # quitando los elementos de la derecha
# # Como una resta
print(primer_set - segundo)

# # Operador Diferencia simétrica
# # Es lo contrario de la intersección.
# # Devolverá los elementos
# # que no se encuentren en los dos sets
print(primer_set ^ segundo)
