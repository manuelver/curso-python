"""
random text generator
=====================
Genera un texto aleatorio a partir de un archivo
de palabras de Linux ubicado en la mayoría
de las distribuciones en /usr/share/dict/words

Pregunta al usuario el número de párrafos
y palabras por párrafo.

Se puede utilizar a modo de lorem ipsum.
"""
import random

# Ruta al archivo de palabras en Linux (puede variar según la distribución)
word_file = '/usr/share/dict/words'

# Función para generar texto aleatorio


def generate_random_text(word_file, num_words=50):
    with open(word_file, 'r') as file:
        words = [line.strip() for line in file.readlines()]

    # Seleccionar un número de palabras al azar
    random_words = random.sample(words, num_words)

    # Combinar las palabras para formar el texto
    random_text = ' '.join(random_words)

    return random_text


# Preguntar al usuario el número de párrafos y palabras por párrafo
num_paragraphs = int(input("Número de párrafos a generar: "))
num_words_per_paragraph = int(input("Número de palabras por párrafo: "))

# Generar los párrafos de texto aleatorio
print("Texto aleatorio generado:")
for _ in range(num_paragraphs):
    random_paragraph = generate_random_text(word_file, num_words_per_paragraph)
    print(random_paragraph, "\n")
