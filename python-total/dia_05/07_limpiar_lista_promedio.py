lista_numeros = [1, 2, 15, 7, 2, 3]


def reducir_lista(lista):

    lista.sort()
    lista_limpia = set(lista)
    max_value = max(lista_limpia)
    lista_limpia.remove(max_value)
    return lista_limpia


def promedio(lista):
    total = 0
    for x in lista:
        total += x
    resultado = total / len(lista)
    return resultado


lista2 = reducir_lista(lista_numeros)
media = promedio(lista2)

print(f"La lista limpia es {lista2}")
print(f"El valor medio de la lista resultante es {media}")

# Otra opción de limpiar la lista


def reducir_lista2(lista):
    lista.sort()
    lista_limpia = []
    for n in lista:
        if n not in lista_limpia:
            lista_limpia.append(n)

    max_value = max(lista_limpia)
    lista_limpia.remove(max_value)
    return lista_limpia


lista3 = reducir_lista2(lista_numeros)

print(f"Otra opción de limpiar la lista: {lista3}")
