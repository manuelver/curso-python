"""
Condicionales con if
"""

edad = input("Introduce tu edad: ")
edad = int(edad)

if edad > 65:
    print("Tienes un super descuento para super seniors")
elif edad > 55:
    print("Tienes un descuento para seniors")
elif edad > 17:
    print("Puedes entrar")
else:
    print("Lo siento, eres menor de edad. Debes irte")
