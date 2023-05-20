"""
Programa día 8 - Turnero

import numeros y funciones

"""
import os
import numeros


def clear_console():
    """ Función limpiar consola """

    limpiar = 'clear'
    os.system(limpiar)


def bienvenida():
    """ Bienvenida e inicio del programa """

    clear_console()

    # bienvenida al usuario
    print(
        '\n',
        '#' * 40,
        '\n #  Bienvenid@ al turnero de farmacia   #\n',
        '#' * 40)

    pausa()

    clear_console()

    nuevo_turno()


def pausa():
    """ Pausar 3 segundos """

    sleep = 'sleep 3'
    os.system(sleep)


def nuevo_turno():
    """ Expendedor de turnos """
    comando = ""
    while comando.lower() != 's':

        clear_console()

        print('¿De qué departamento quieres el turno?\n',
              '\n DEPARTAMENTO\t| COMANDO',
              '\n----------------|---------',
              '\n Perfumería\t| [p]',
              '\n Farmacia\t| [f]',
              '\n Cosmética\t| [c]\n')
        comando = input("> ")
        if comando.lower() == 'p':
            numeros.turnos('perfumeria')

        elif comando.lower() == 'f':
            numeros.turnos('farmacia')

        elif comando.lower() == 'c':
            numeros.turnos('cosmetica')

        elif comando.lower() == 's':
            print('Gracias por usar el turnero')
            break

        else:
            print('Inserta un valor válido')

        pausa()


bienvenida()
