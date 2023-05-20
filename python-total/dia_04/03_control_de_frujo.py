"""
Control de flujo

if condición:
    print(codigo)
elif otra_condición:
    print(codigo)
else:
"""

x = True


if 5 == 2:
    print("Es correcto")
else:
    print("Parece que es falso")

edad = input("Dime tu edad: ")
edad = int(edad)

if edad <= 17:
    print("Eres menor de edad")
    calificacion = input("Que nota sacaste? ")
    calificacion = int(calificacion)
    if calificacion >= 5:
        print("Felicitaciones! Has aprobado")
    else:
        print("No aprobado")
else:
    print("Eres adulto")
