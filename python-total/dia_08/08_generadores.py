"""
Funciones generadoras

se iteran pero espera a ejecutar al momento que se le pide

Utiliza yield (Construir) para retornar 
y devuelve con next

"""


def mi_funcion():
    for x in range(1, 5):
        yield x * 10


def mi_generador():
    for i in range(1, 4):
        yield i


h = mi_funcion()

print(next(h))

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))

print()


# Otro ejemplo


def mi_generation():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


i = mi_generation()

print(next(i))
print(next(i))
print(next(i))


print()

# Ejercicio 1


def infinito():
    i = 0
    while i != -1:
        i += 1
        yield i


generador = infinito()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


print()

# Ejercicio 2


def infinito_siete():
    i = 0
    resultado = 7
    while i != -1:
        i += 1
        resultado = 7 * i
        yield resultado


generador = infinito_siete()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


print()

# Ejercicio 2


def vidas():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"


vida = vidas()

print(next(vida))
print(next(vida))
print(next(vida))
print(next(vida))
