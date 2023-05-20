"""
Calculadora

Seudocódigo:
    Aplicación interactiva, tenemos que escribir constantemente en la terminal.
    Verificar si se ha ingresado un número
    Si no hay número pedir el número y después pedir operación +-*/
    Si ya hay un número pedir operación +-*/
    Pedir otro número
    Mostrar resultado y guardar como el primer número

"""
import time
# Bienvenida
print("\n############################")
print("Bienvenidos a la calculadora")
print("############################")
print("\nPara salir tan solo tienes que escribir (salir)")

# Pedir el primer número y opciones de operación
n1 = input("\nIngresa el primer número: ")
print(f"Vamos a operar con el {n1}")
print("\nLas operaciones que puedes realizar son:")
print("- Sumar       --> (s)")
print("- Restar      --> (r)")
print("- Multiplicar --> (m)")
print("- Dividir     --> (d)\n")


# Inicio de bucle. Si no se pone "salir" seguirá dentro
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    if comando != "salir":
        op = comando

        if op not in ("s", "r", "m", "d"):
            print("\nDime un operador correcto")
            continue
        
        print(f"\nVamos a realizar la operación con el número {n1}")
        n2 = input("Dime el segundo número: ")

        # Conversor de str a int de los números 
        n2 = int(n2)
        n1 = int(n1)

        # Posibles operaciones
        suma = n1 + n2
        resta = n1 - n2
        multi = n1 * n2
        div = n1 / n2

        # Condicional de las respuestas a las operaciones
        if op == "s":
            print(f"__________________________________________________")
            print(f"\nEl resultado de la suma de {n1} y {n2} es {suma}")
            print(f"__________________________________________________")
            time.sleep(1.5)
            print("\n Dime otro operador")
            n1 = suma
        elif op == "r":
            print(f"__________________________________________________")
            print(f"\nEl resultado de la resta de {n1} y {n2} es {resta}")
            print(f"__________________________________________________")
            time.sleep(1.5)
            print("\n Dime otro operador")
            n1 = resta
        elif op == "m":
            print(f"__________________________________________________")
            print(f"\nEl resultado de la multiplicación entre {n1} por {n2} es {multi}")
            print(f"__________________________________________________")
            time.sleep(1.5)
            print("\n Dime otro operador")
            n1 = multi
        elif op == "d":
            print(f"__________________________________________________")
            print(f"\nEl resultado de la división entre {n1} por {n2} es {div}")
            print(f"__________________________________________________")
            time.sleep(1.5)
            print("\n Dime otro operador")
            n1 = div

    # Despedida de la opción "salir" 
    elif comando == "salir":
        print("\nHasta pronto! ^_^")
        break
    # Error, si se pone un comando diferente a todo lo anterior
    else:
        print(f"\nQue me estás container?")
        print("Estas son las opciones:")
        print("- Sumar       --> (s)")
        print("- Restar      --> (r)")
        print("- Multiplicar --> (m)")
        print("- Dividir     --> (d)")
        print("- Salir       --> (salir)\n")
        continue
