"""
Calculadora
Solución al ejercicio

Seudocódigo:
    Aplicación interactiva, tenemos que escribir constantemente en la terminal.
    Verificar si se ha ingresado un número
    Si no hay número pedir el número y después pedir operación +-*/
    Si ya hay un número pedir operación +-*/
    Pedir otro número
    Mostrar resultado y guardar como el primer número

"""
# Bienvenida
print("\n############################")
print("Bienvenidos a la calculadora Hola Mundo")
print("############################")
print("\nPara salir tan solo tienes que escribir (salir)")
print("\nLas operaciones que puedes realizar son s, r, m y d")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "s":
        resultado += n2
    elif op.lower() == "r":
        resultado -= n2
    elif op.lower() == "m":
        resultado *= n2
    elif op.lower() == "d":
        resultado /= n2
    else:
        print("Operación no válida")
        break

    print(f"El resultado es {resultado}")
