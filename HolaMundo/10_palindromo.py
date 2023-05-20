"""
Comprobar palindromo
"""


def es_palindromo(texto):
    """
    Función para comprobar si es un palindromo
    Al texto se le elimina los espacios y acentos
    """
    # Sustituyo vocales con acento y pongo texto en minúsculas
    texto = texto.replace('á', 'a').replace('é', 'e').replace(
        'í', 'i').replace('ó', 'o').replace('ú', 'u').lower()

    # Declaro variables
    al_derecho = ''
    al_reves = ''

    # Ordeno el texto al derecho y al revés sin espacios
    for i in texto:
        if i != ' ':
            al_reves = i + al_reves
            al_derecho += i

    # Comparo el texto al derecho y al revés
    return al_derecho == al_reves

    # Explicacion
print("Este programa comprueba si el texto que introduzcas es un palindromo")
print("Para salir debes introducir \"salir\"\n")


# Bucle con la pregunta de la palabra, con la condicional true/false
# de respuesta y con otra pregunta por si quiere preguntar más.

txt = ''
while txt.lower() != 'salir':
    txt = input('Dame un texto para comprobar si es palindromo: ')

    print()
    if txt == 'salir':
        break
    elif es_palindromo(txt):
        print(f'El texto \"{txt}\" es palindromo')
    else:
        print(f'El texto \"{txt}\" no es palindromo')
    print()

print('¡Ciao!')
