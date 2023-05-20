"""
Problemas prácticos
"""

# Ejercicio ############
# Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
# Si la suma de los 3 números es mayor a 15, va a devolver el número mayor.
# Si la suma de los 3 números es menor a 10, va a devolver el número menor.
# Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio.


def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


print(devolver_distintos(6, 5, 3))


# Ejercicio 2 ############
# Escribe una función (puedes ponerle cualquier nombre que quieras)
# que reciba cualquier palabra como parámetro,
# y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra "entretenido",
# debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']

def cualquier(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)

    lista = list(mi_set)
    lista.sort()
    return lista


print("\n")
print(cualquier('entretenido'))
print(cualquier('cascarrabias'))


# Ejercicio 3 ############
# Escribe una función que requiera una cantidad indefinida de argumentos.
# Lo que hará esta función es devolver True
# si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def me_gustan_los_ceros(*ceros):

    contador = 0
    for num in ceros:

        if num == 0:
            contador += 1
            if contador == 2:
                contador = 0
                return True
        elif num != 0:
            contador = 0
        else:
            pass

    return False


print("\n")
print(me_gustan_los_ceros(5, 6, 1, 0, 0, 9, 3, 5))
print(me_gustan_los_ceros(6, 0, 5, 1, 0, 3, 0, 1))

# Solución curso


def ceros_vecinos(*args):
    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False


print("\n")
print(ceros_vecinos(5, 6, 1, 0, 0, 9, 3, 5))
print(ceros_vecinos(6, 0, 5, 1, 0, 3, 0, 1))


# Ejercicio 4 ############
# Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números primos existentes
# en el rango que va desde cero hasta ese número incluido,
# y va a devolver la cantidad de números primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.


def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True


def primos(rango_max):
    rango_max += 1

    lista_num = [n for n in range(1, rango_max)]

    primos = []

    for numero in lista_num:
        es_primo = primo(numero)
        if es_primo:
            primos.append(numero)
    contar = len(primos)

    rango_max -= 1
    print(f"\nEntre 0 y el {rango_max} hay {contar} números primos:")

    print(*primos, sep=' ')


primos(1000)


# Solución curso

def contar_primos(numero):
    primos2 = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos2.append(iteracion)
            iteracion += 2

    print(primos2)
    return len(primos2)


print("\n")
print(contar_primos(1000))
