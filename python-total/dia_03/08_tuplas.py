mi_tuple = (1,2,3,4)
mi_tuple2 = 1,2,(10,20),4
print(type(mi_tuple))
print(mi_tuple2)

print(mi_tuple[2])
print(mi_tuple[-2])

print(mi_tuple2[2][0])

# El tuple se puede convertir en una lista
mi_tuple =list(mi_tuple)
print(type(mi_tuple))
# También al revés, se puede convertir una lista en un tuple
mi_tuple =tuple(mi_tuple)
print(type(mi_tuple))

# Se puede dar cada uno de los valores a una variable distinta
# pero tienen que coincidir la cantidad de valores con las variables
t = 1,2,1
x,y,z = t
print(x, y, z)

# Se puede pedir el número de elementos
print(len(t))

# Se puede contar la cantidad de apareciones de un valor
print(t.count(1))

# También se puede consultar el indice de un valor
print(t.index(2))


