"""
Random Password Generator
=========================
Genera una contraseña aleatoria con el número 
de palabras que indiques a partir de un archivo
de palabras de Linux ubicado en la mayoría 
de las distribuciones en /usr/share/dict/words

Despues, pregunta al usuario si desea mezclar
las letras de la contraseña generada.
"""
import random

# Ruta al archivo de palabras en Linux (puede variar según la distribución)
word_file = '/usr/share/dict/words'

# Función para generar una contraseña aleatoria


def generate_password(word_file, num_words):
    with open(word_file, 'r') as file:
        words = [line.strip() for line in file.readlines()]

    # Seleccionar un número de palabras al azar
    password_words = random.sample(words, num_words)

    # Combinar las palabras para formar la contraseña
    password = ''.join(password_words)

    return password

# Función para mezclar las letras de una cadena


def shuffle_letters(input_string):
    letters = list(input_string)
    random.shuffle(letters)
    return ''.join(letters)


# Preguntar al usuario cuántas palabras desea en la contraseña
num_words = int(input("Número de palabras para la contraseña: "))

# Generar una contraseña aleatoria con el número de palabras especificado
random_password = generate_password(word_file, num_words)
print("Contraseña aleatoria generada:", random_password)

# Preguntar al usuario si desea mezclar las letras
mezclar_letras = input(
    "¿Desea mezclar las letras de la contraseña? (s/n): ").lower()
if mezclar_letras == 's':
    random_password = shuffle_letters(random_password)
    print("Contraseña con letras mezcladas:", random_password)
