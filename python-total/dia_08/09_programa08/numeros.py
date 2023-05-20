"""
Programa día 8 - Turnero

Generadores y decorador

"""


def perfumeria():
    """ Turnos de perfumeria """

    turno_p = -1

    while True:
        turno_p += 1
        yield f'P-{turno_p}'


def farmacia():
    """ Turnos de farmacia """

    turno_f = -1

    while True:

        turno_f += 1
        yield f'F-{turno_f}'


def cosmetica():
    """ Turnos de cosmetica """

    turno_c = -1
    while True:

        turno_c += 1
        yield f'C-{turno_c}'


def turnos(dpto):
    """Turnos perfumeria"""

    print('Su turno es ')

    if dpto == 'perfumeria':

        print(next(perf))

    elif dpto == 'farmacia':

        print(next(farm))

    elif dpto == 'cosmetica':

        print(next(cos))

    else:
        print('Error')

    print('Aguarde y será atendido')


# Variables
perf = perfumeria()
farm = farmacia()
cos = cosmetica()


turnos('perfumeria')
turnos('farmacia')
turnos('cosmetica')
