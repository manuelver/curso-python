# LAS LISTAS
lista_1 = ["C", "C++", "Python", "Java"]
lista_2 = ["PHP", "SQL", "Visual Basic"]
lista_3 = ["d", "a", "c", "b", "e"]
lista_4 = [5, 4, 7, 1, 9]

# Ver tipo de dato de las listas
print(type(lista_1))

# Concatenar listas
lista_1_2 = lista_1 + lista_2
print(lista_1_2)

# EN LAS LISTAS SE PUEDEN MODIFICAR LOS ELEMENTOS
# Agregar un elemento a la lista
lista_1.append("R")
print(lista_1)

# Eliminar un elemento de la lista con el índice (Devuelve el valor eliminado)
print(lista_1.pop(4))

guardar_elemento = lista_1_2.pop(2)
print(guardar_elemento)

# Ordenar los elementos de la lista
lista_3.sort()
print(lista_3)
# Cuidado que no devuelve nada, modifica la variable
guardar_sort = lista_3.sort()
print(guardar_sort)
# Es de tipo None, un objecto sin valor, que no es lo mismo que 0
print(type(guardar_sort))

# Invierte el orden de los elementos (No es lo opuesto a sort)
lista_4.reverse()
print(lista_4)
