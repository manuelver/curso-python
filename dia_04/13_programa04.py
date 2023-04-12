"""
Programa día 4 - Juego "Adivina el número"
"""
# Importamos módulos
from random import randint
import itertools
import threading
import time
import sys
import os


# Funciones

# Función limpiar consola
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Función de la animación para 'pensar'


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if DONE:
            break
        sys.stdout.write('\rPensando un número ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rYa tengo el número!                 ')
    sys.stdout.write('\nA ver si aciertas, dime un número: ')


# Función validar input es un número
def validar(dato, tipos):
    for tipo in tipos:
        try:
            return tipo(dato)
        except ValueError:
            pass
    return None


#  Limpiar la terminal
clearConsole()

# Mensaje bienvenida
print("\n#########################")
print("JUEGO - Adivina el número")
print("#########################\n")

# Pregunta nombre, saluda y explica el juego (Con opción a salir)
nombre = input("¿Cuál es tu nombre? ")
print(f"\nOk {nombre}, voy a pensar un número del 1 al 100.")
print("Tienes 8 intentos para adivinarlo\n")

# Filigrana como que piensa la máquina

DONE = False
t = threading.Thread(target=animate)
t.start()

# El tiempo de ejecución
time.sleep(3)
DONE = True

# Guardando el número secreto
n_secreto = randint(1, 100)

# Bucle de intentos y control de flujo
for intentos in range(8):

    # Calcular intentos restantes
    lista_intentos = list(range(8))
    lista_intentos.reverse()
    intentos_restantes = lista_intentos.pop(intentos)

    # Pregunta posible número y valida que es de type número
    while True:
        n_posible = input("Dime un número: ")
        x = validar(n_posible, (int, float, complex))
        if x is None:
            print("Error: El dato introducido no es un número\n")
        else:
            break

    # Para comparar el número se necesita que sea integer
    n_posible = int(n_posible)

    # Posibles casuísticas
    # Si el número no está en el rango especificado
    if (n_posible < 1) or (n_posible > 100):
        print("\nEse número no está entre el 1 y el 100")
        print(
            f"Desperdiciaste un turno, te quedan {intentos_restantes} intentos")

    # Si el número es menor
    elif n_posible > n_secreto:
        print(
            f"\nLo siento, has fallado.Te quedan {intentos_restantes} intentos.")
        print("\n\tPista --> El número es menor.\n")

    # Si el número es mayor
    elif n_posible < n_secreto:
        print(
            f"\nLo siento, has fallado.Te quedan {intentos_restantes} intentos.")
        print("\n\tPista --> El número es mayor.\n")

    # Si se acierta el número
    elif n_posible == n_secreto:
        print("\n¡Ole! ¡¡¡¡HAS ACERTADO!!!!")
        intentos += 1
        print(f"¡Felicidades {nombre}!\nLo conseguiste en {intentos} intentos")
        break

    # Si se agotan los intentos
    if intentos == 7:
        print(
            f"\n¡Vaya! Has gastado los 8 intentos.\nEl número pensado era el {n_secreto}.\n Otra vez será...\nCiao!")

print("\n¡Espero que te hayas divertido!")
