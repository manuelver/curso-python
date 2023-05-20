"""
Interacción entre funciones

Programa "Escoge un palito"
"""
from random import shuffle

# Lista inicial y presentación
palitos = ['-','--','---','----']

print("¡Hola!\n")
print(f"Tenemos estos palitos:")
for palito in palitos:
    print(palito)
print("\nVamos a mezclarlos y a relacionarlos con un número.\n")

# Mezclar palitos
def mezclar(lista):
    shuffle(palitos)
    return lista

# Pedir al usuario intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un número del 1 al 4: ")
        if intento not in ['1','2','3','4']:
            print("\nError: Ingresa un valor válido\n")
        else:
            pass
    return int(intento)

# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("¡Cogiste el palito más corto!\n")
    else:
        print("Lo siento, no es el más corto: \n")

    print(lista[intento-1])
    print()

# Invocamos las funciones

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)
