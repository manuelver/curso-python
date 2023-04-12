"""
Numeros para práctica
"""


def numeros_perfumeria():
    """Esto es un comentario"""
    for numeros_perfum in range(1, 10000):
        yield f"P - {numeros_perfum}"


def numeros_farmacia():
    """Esto es un comentario"""
    for numeros_farma in range(1, 10000):
        yield f"F - {numeros_farma}"


def numeros_cosmetica():
    """Esto es un comentario"""
    for numeros_cosmetic in range(1, 10000):
        yield f"C - {numeros_cosmetic}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(rubro):
    """Esto es un comentario"""

    print("\n" + "*" * 23)
    print("Su número es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")
