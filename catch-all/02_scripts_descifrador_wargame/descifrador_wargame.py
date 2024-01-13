#!/usr/bin/env python3
"""
Lo siento, acabo de ver "Juegos de Guerras" y me he emocionado.
Este programa descifra un código de números y letras mayúsculas aleatorio.
El código se descifra letra por letra y número por número.
Se utiliza random para generar los números y letras aleatorias, 
para que tenga más emoción.
"""

import os
import random


def code_clear():
    """
    Crear un código de números y letras mayúsculas aleatorio
    """

    os.system('clear')


def number_generate():
    """
    Genera un número aleatorio entre 0 y 9
    """

    number_random = str(random.randint(0, 9))
    # number_random = chr(random.choice(string.ascii_letters + string.digits))

    return number_random


def upper_letter_generate():
    """
    Genera una letra mayúscula aleatoria entre A y Z
    """
    letter_random = chr(random.randint(65, 90))

    return letter_random


def lower_letter_generate():
    """
    Genera una letra minúscula aleatoria entre a y z
    """
    letter_random = chr(random.randint(97, 122))

    return letter_random


def mecanografiar(msg):
    for i in range(0, len(msg)):
        code_clear()
        print(msg[:i])
        os.system('sleep .1')


def descifrador(codigo):
    """
    Descifra el código
    """

    numero_caracteres = len(codigo)
    codigo_decode = " " * numero_caracteres
    while True:

        for i in range(0, len(codigo)):

            if codigo[i] == codigo_decode[i]:

                codigo_decode = codigo_decode[:i] + \
                    codigo[i] + codigo_decode[i + 1:]

            elif codigo[i].isalpha():

                if codigo[i].isupper():

                    codigo_decode = codigo_decode[:i] + \
                        upper_letter_generate() + codigo_decode[i + 1:]
                else:
                    codigo_decode = codigo_decode[:i] + \
                        lower_letter_generate() + codigo_decode[i + 1:]

            elif codigo[i].isdigit():

                codigo_decode = codigo_decode[:i] + \
                    number_generate() + codigo_decode[i + 1:]

            else:

                codigo_decode[i] = " "

        code_clear()
        print(codigo_decode)
        os.system('sleep .1')
        if codigo_decode == codigo:
            break

    code_clear()
    return f"El código descifrado es: {codigo_decode}"


def mensaje_final():

    os.system('sleep 3')
    mecanografiar("Los mísiles nucleares se lanzarán en 5 segundos.  ")
    os.system('sleep 1')

    for i in range(5, 0, -1):
        code_clear()
        print(i)
        os.system('sleep 1')

    mecanografiar("Los mísiles nucleares se han lanzado.  ")
    os.system('sleep 3')

    mecanografiar("Los mísiles nucleares han impactado.  ")
    os.system('sleep 1.5')

    mecanografiar("La humanidad ha sido destruida.  ")
    os.system('sleep 1.5')

    mecanografiar("Fin del programa.  ")
    os.system('sleep 1.5')

    mecanografiar("¡Hasta la vista, baby! 💋💋💋 ")


def main():
    """
    Función principal
    """

    code_clear()
    print(("#"*36) + "BIENVENIDO AL DESCIFRADOR DE CÓDIGOS" + ("#"*36))
    CODIGO = input("Introduzca el código a descifrar: ")

    print(descifrador(CODIGO))

    mensaje_final()


if __name__ == "__main__":
    main()
