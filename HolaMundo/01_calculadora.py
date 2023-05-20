"""
Calculadora
"""

# Se piden los valores
n1 = input("Ingresa el primer número: ")
n2 = input("Ingresa el segundo número: ")

# Se transforman los valores en integer
n1 = int(n1)
n2 = int(n2)

# Variables de las posibles operaciones
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

# Se pregunta la operación a realizar
op = input("""
¿Qué operación quieres hacer?
s --> Sumar
r --> Restar
m --> Multiplicar
d --> Dividir
>  """)

opciones = ("s", "r", "m", "d")

if op == "s":
    print(f"El resultado de la suma de {n1} y {n2} es {suma}")
elif op == "r":
    print(f"El resultado de la resta de {n1} y {n2} es {resta}")
elif op == "m":
    print(f"El resultado de la multiplicación entre {n1} por {n2} es {multi}")
elif op == "d":
    print(f"El resultado de la división entre {n1} por {n2} es {div}")
else:
    print("Operación no encontrada. Vuelve a intentarlo")
