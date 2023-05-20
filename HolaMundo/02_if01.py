"""
Condicionales con if
"""

edad = input("Introduce tu edad: ")
edad = int(edad)
if edad > 17:
    print("Puedes ver la pelicula. Adelante!")
    if edad >= 55:
        print("Ademas, no olvides pedir el descuento para seniors")
else:
    print("Lo siento, eres menor de edad")
