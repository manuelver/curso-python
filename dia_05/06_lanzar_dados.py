"""
Interacción entre funciones
LANZAR DOS DADOS
"""
from random import randint

# Función para obtener dos valores aleatorios
# entre el 1 y el 6


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    return dado1, dado2

# Función para evaluar la tirada


def evaluar_jugada(num1, num2):
    suma_dados = num1 + num2
    text1 = "La suma de tus dados es "
    if suma_dados <= 4:
        suma_dados = str(suma_dados)
        mensaje = text1 + suma_dados + ". \nLamentable\n"
    elif suma_dados > 4 and suma_dados <= 7:
        suma_dados = str(suma_dados)
        mensaje = text1 + suma_dados + ". \nBueno... esta bien.\n"
    elif suma_dados > 7 and suma_dados < 10:
        suma_dados = str(suma_dados)
        mensaje = text1 + suma_dados + ". \nBuena tirada!\n"
    else:
        suma_dados = str(suma_dados)
        mensaje = text1 + suma_dados + ". \nParece una jugada ganadora\n"

    return mensaje


# Presentación
print("¡Vamos a tirar los dados!\n")

bandera = 's'
while bandera.lower() != "n":

    # Control de flujo
    if bandera.lower() == 's':
        # Recogida de los valores
        n1, n2 = lanzar_dados()
        resultado = evaluar_jugada(n1, n2)
        print(f"{resultado}")
    elif bandera.lower() != 'n' or bandera.lower() != 's':
        print("¿Que me estás contando?\n\t Sí ---> s\n\t No ---> n")
        bandera = 's'
    else:
        print("\n¡Ciao!")
        break

    # Pregunta si quieres seguir jugando
    bandera = input("¿Quieres tirar de nuevo? (s/n) ")
