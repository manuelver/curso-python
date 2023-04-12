"""
Argumentos indeterminados

*args      --->  Arguments
Para definir funciones que acepten
un número indeterminado de variables

**kwargs   --->  Keyword arguments
Definen funciones que acepten
diccionarios. Podemos añadir un número indeterminado
de variables y de key=value
"""

# Ejemplo de *args
# Argumentos args es una tupla, no se puede modificar


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


calculo = suma(24, 45, 22, 43, 454, 23, 12)

print(calculo)

# Ejercicio 1 - Suma cuadrados


def suma_cuadrados(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero**2

    return resultado


print(suma_cuadrados(1, 2, 3))


# Ejercicio 2 - Suma solo absolutos

def suma_absolutos(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += abs(numero)

    return resultado


print(suma_absolutos(1, -2, 3))

# Ejercicio 3 - mezclar variable y *args


def numeros_persona(nombre, *numeros):
    suma_numeros = 0
    for numero in numeros:
        suma_numeros += numero

    suma_numeros = str(suma_numeros)
    para_devolver = nombre + " la suma de tus números es " + suma_numeros
    return para_devolver


print(numeros_persona("Mun", 1, 3, 4, 2, 4))


# Ejemplo de **kwargs - Explicación conceptual
# Cuando pasamos los valores al kwargs
# este lo convierte en diccionario

def suma_dic(**kwargs):
    print(type(kwargs))


suma_dic(x=3, y=5, z=2)

# Otro ejemplo


def suma_diccio(**kwargs):

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        total += valor
    return total


print(suma_diccio(x=3, y=5, z=2))


# Con lo cual, también podemos añadir
# - Parámetros
# - *args
# - **kwargs
# Y todo en la misma función
# Deberían seguir siempre este orden

def prueba(num1, num2, *args, **kwargs):

    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f"arg es igual a {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")


prueba(15, 50, 100, 200, 300, 400, x='uno', y='dos', z='tres')


# Truco para desempacar listas o tuplas
# Poner los astericos en los argumentos que se le pasa a la función

def la_lista(*lista, **dic):

    for arg in lista:
        print(f"arg es igual a {arg}")

    for clave, valor in dic.items():
        print(f"{clave} es igual a {valor}")


para_args = [1000, 2000, 3000, 4000]
kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

la_lista(*para_args, **kwargs)


# Ejercicio 1 - cantidad de atributos

def cantidad_atributos(**cuentas):
    contador = 0
    for x in cuentas.items():
        contador += 1
    return contador

    print(len(cuentas))


print(cantidad_atributos(x='color_ojos'))

# Ejercicio 2 - Lista atributos de values


def lista_atributos(**lista):
    listado = []
    for clave in lista.values():
        listado.append(clave)
    return listado


print(lista_atributos(x='uno', y='dos', z='tres'))

# Ejercicio 3 -


def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')

    for nombre_argumento, valor_argumento in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')


describir_persona("María", color_ojos="azules", color_pelo="rubio")
