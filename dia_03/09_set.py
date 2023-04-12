""" Sets """

mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))
print(mi_set)

# No acepta repeticiones
# No acepta listas 
# pero sí tuples porque son inmutables
otro_set = set([1, 2, 3, 4, 5, (1,2,3), 1, 1, 1])
print(otro_set)

print(len(mi_set))

print(2 in mi_set)

# MÉTODOS

# Union
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# Agregar
s1.add(4)
print(s1)

# Eliminar. Si no encuentra el elemento
# da error
s1.remove(3)
print(s1)

# Descartar. Funciona como remove 
# pero no da error si no encuentra el elemento
s1.discard(3)
print(s1)

# Elimina un elemento aleatorio
sorteo = s1.pop()
print(sorteo)
print(s1)

# Vaciar el set
s1.clear()
print(s1)
