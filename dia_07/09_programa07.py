"""
Programa día 7 - Cuenta bancaria

ESTAFA BANK
"""
import os


""" Variables """
limpiar = 'clear'
sleep = 'sleep 2'

""" Clases """


class Persona:

    # Atributos: nombre y apellido
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    # atributos propios: número de cuenta y balance
    # es decir, el saldo que tiene en su cuenta bancaria.
    def __init__(self, nombre, apellido, num_cuenta, balance):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = float(round(balance, 2))

    # tres métodos
    # # método especial que permite que podamos imprimir a nuestro cliente
    def __str__(self):
        return f'***  CLIENTE ESTAFA BANK  ***\n\n\tCliente: \t{self.nombre} {self.apellido}\n\tNº Cuenta: \t{self.num_cuenta}\n\tBalance: \t{self.balance} pesos'

    # # Método Depositar que permita decidir cuánto dinero quiere agregar a su cuenta

    def depositar(self, cantidad_ingreso):
        self.balance += cantidad_ingreso
        self.balance = round(self.balance, 2)
        print(
            f'\nHa ingresado {cantidad_ingreso} Pesos.\n')

    # # Método llamado Retirar que permita decidir cuánto dinero quiere sacar de su cuenta

    def retirar(self, cantidad_a_retirar):
        if (self.balance - cantidad_a_retirar) < 0:
            print(
                f'\nDisculpa, no tienes tanto dinero.\nBalance: {self.balance} pesos')
        else:
            self.balance -= cantidad_a_retirar
            self.balance = round(self.balance, 2)
            print(
                f'\nHa retirado {cantidad_a_retirar} Pesos.\n')


""" Funciones """


def clearConsole():
    # Función limpiar consola
    os.system(limpiar)


def bienvenida():

    clearConsole()

    # bienvenida al usuario
    print(
        '\n',
        '#' * 39,
        '\n #   Bienvenid@ a tu cuenta bancaria   #\n',
        '#' * 39)

    os.system(sleep)

    clearConsole()

    # Iniciar programa pidiendo datos del cliente
    crear_cliente()

    # Pedir operaciones a realizar - PROGRAMA
    operaciones()


def despedida():
    clearConsole()

    print('Gracias por usar los servicios de ESTAFA BANK, su banco sincero.\n\n¡Ciao!\n')


def crear_cliente():

    nombre_cliente = input("Dime tu nombre: ")
    apellido_cliente = input("Dime tu/s apelludo/s: ")

    global cliente1

    cliente1 = Cliente(
        nombre_cliente,
        apellido_cliente,
        '324789563417896324',
        0)


def operaciones():

    # PROGRAMA
    # Pedir al usuario que elija si quiere hacer depósitos o retiros.

    operacion = ''
    while operacion.lower() != 's':
        print(
            f'\n',
            cliente1,
            '\n\n Indicar la operación a realizar:\n',
            '\n\t- i\t-->\tIngresar'
            '\n\t- r\t-->\tRetirar'
            '\n\t- s\t-->\tSalir\n')

        operacion = input()

        operacion = operacion.lower()

        if operacion == "i":
            cantidad_a_ingresar = preguntar_cantidad('ingresar')
            cliente1.depositar(cantidad_a_ingresar)
            continue

        elif operacion == "r":
            cantidad_a_retirar = preguntar_cantidad('retirar')
            cliente1.retirar(cantidad_a_retirar)
            continue

        elif operacion == "s":
            break

        else:
            clearConsole()
            print('Disculpa, ingresa un valor valido\n')
            continue
    despedida()


def preguntar_cantidad(ope):

    clearConsole()

    print(
        f'\nSu balance actual es de {cliente1.balance} Pesos.\n\n',
        f'¿Qué cantidad quiere {ope}?')

    cantidad = input()

    cantidad = round(float(cantidad), 2)

    return cantidad


""" Programa - Se inicia a través de la función de bienvenida """


# Bienvenida e iniciar programa
bienvenida()
