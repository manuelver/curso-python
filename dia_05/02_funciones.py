"""
funciones
"""

# Simpple

def suma5(nombre):
    """
    Esto es una función para decir hola
    """
    print("Hola! " + nombre)

name = input("Dime tu nombre: ")

for i in range(5):
    suma5(name)

# return
def sumar(num1,num2):
    total =  num1 + num2
    return total

resultado = sumar(10,5)

print(resultado)

#   Ejercicio de codificación
def invertir_palabra(palabra):
    reverso = palabra[::-1]
    return reverso

print(invertir_palabra("Python").upper())
