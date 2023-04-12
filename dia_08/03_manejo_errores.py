"""
Manejo de errores

Intentar        --> try

Excepción       --> except

Finalmente      --> finally

"""


def suma():
    n1 = int(input('El numero 1: '))
    n2 = int(input('El numero 2: '))
    print(n1 + n2)
    print('Gracias por sumar' + n1)


try:
    # Codigo que queremos probar
    suma()
except TypeError:
    # Código a ejecutar si hay un error
    print('Estas intentando concatenar tipos distintos')
except ValueError:
    # Código a ejecutar si hay un error
    print('Estas intentando sumar algo que no son números?')
else:
    # Código a ejecutar si no hay un error
    print('Hiciste todo bien')
finally:
    # Código que se va a ejecutar de todos modos
    print('Eso fue todo')


# Ejemplo para pedir un número de manera correcta

def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un número: '))
        except:
            print('\nEse no es un número')
        else:
            print(f'Ingresaste el número {numero}')
            break


print('Gracias')

pedir_numero()
