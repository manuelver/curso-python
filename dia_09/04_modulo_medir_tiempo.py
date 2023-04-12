"""
Módulo para medir tiempo

time - puedes realizar marcas de tiempo en el código
para poder hacer comparaciones

timeit - Más especifico, muestra cuanto tarda en ejecutarse un código.

"""

import time
import timeit

# Dos funciones con formas distintas
# de hacer código
# para el mismo resultado:


def prueba_for(numero):
    """ Prueba de iteración for """
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista


def prueba_while(numero):
    """ Prueba de iteración while """
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


# Vamos a identificar cual de las dos funciones
# resuelve de manera más eficiente
# con el módulo time, haciendo
# marcas de tiempo
inicio = time.time()
prueba_for(1000000)
final = time.time()
print(f' La función for tardó: {final - inicio}')

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(f' La función while tardó: {final - inicio}')


print()
# timeit puede identificar
# cuanto tarda con más precisión
"""
Sintaxis:

duracion = timeit.timeit(declaracion, setup, number = numero)

declaracion: recibe el código que cuya duración 
de ejecución queremos medir.
	→ es la invocación mi función

setup: recibe las instrucciones que el parámetro 
declaracion requiere para funcionar.
	→ es la definición (def...) de mi función

number: cantidad de veces que se evaluará el 
código para obtener su tiempo de ejecución mínimo.
	→ pueden ser varios miles o cientos de veces (dependiendo de la complejidad)
"""

declaracion = '''
prueba_for(10)
'''

mi_setup = ''' 
def prueba_for(numero):
    """ Prueba de iteración for """
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
'''

duracion_for = timeit.timeit(declaracion, mi_setup, number=10000000)

print(f' La función for tardó: {duracion_for}')


declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = ''' 
def prueba_while(numero):
    """ Prueba de iteración while """
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion_while = timeit.timeit(declaracion2, mi_setup2, number=10000000)

print(f' La función while tardó: {duracion_while}')
