from random import choice


def lanzar_moneda():
    lista = ['Cara', 'Cruz']
    cara_moneda = choice(lista)
    return cara_moneda


def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        print('La lista se autodestruirá')
        lista.clear()
    elif resultado == 'Cruz':
        print("La lista fue salvada")
    else:
        pass

    return lista


lista_numeros = [1, 3, 5, 2, 3, 145]
mon = lanzar_moneda()
mensaje = probar_suerte(mon, lista_numeros)

print(mon, mensaje)
