"""
funciones Dinamicas
"""

# Simple, comprobar numeros de 3 cifras
def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 347 + 231

resultado = chequear_3_cifras(suma)
print(resultado)


# Comprobar de listas si los numeros tienen 3 cifras
# return hará que se pare el bucle, como un break
def chequear_3_cifras_listas(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    # Para que el return false funcione bien debería estar indentado aquí


lista_num = [1,34,21,15,23,2000]
comprobacion = chequear_3_cifras_listas(lista_num)
print(comprobacion)

## Siendo falso dará un tipo None
print(type(comprobacion))
## No tenía un return False


# Ejercicio comprobar positivos
def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True

lista_posibles_pos = [13,234,5343,7276,-1]

print(todos_positivos(lista_posibles_pos))

# Ejercicio sumar numeros entre 0 y 1000

def suma_menores(lista):
    resultado2 = 0
    for num in lista:
        if num > 0 and num < 1000:
            resultado2 += num
        else:
            pass
    return resultado2
    
lista_numeros = [13,234,5343,7276,-1]
ver = suma_menores(lista_numeros)
print(ver)
