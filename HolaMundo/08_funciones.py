
# Parámetros por defecto
def hola(nombre="Mun", apellido=""):
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}!")


# Argumento indicando el parámetro concreto
hola(apellido="García")

print("")

hola("Mariano", "Bermudez")

hola()

# Parámetro comodín (iterable)
# para añadir un número indeterminado de argumentos.
# xargs


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


print(suma(3, 6, 2, 4, 65, 23, 4, 100))
