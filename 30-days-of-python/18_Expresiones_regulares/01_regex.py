"""
01_regex.py
"""
import re


# Ejercicios: Nivel 1

# 1. ¿Cuál es la palabra más frecuente en el siguiente párrafo?

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Convertimos el párrafo a minúsculas
paragraph = paragraph.lower()

# Separamos el párrafo en palabras
words = paragraph.split()

# Creamos un diccionario para contar la frecuencia de cada palabra
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Encontramos la palabra más frecuente
most_freq_word = max(word_freq, key=word_freq.get)

print("La palabra más frecuente es:", most_freq_word)


# 2. La posición de algunas partículas
# en el eje x horizontal son - 12, -4, -3 y - 1
# en la dirección negativa,
# 0 en el origen,
# 4 y 8 en la dirección positiva.
# Extrae estos números de todo el texto
# y encuentra la distancia entre
# las dos partículas más lejanas.


text = "La posición de algunas partículas en el eje x horizontal son -12, -4, -3 y -1 en la dirección negativa, 0 en el origen, 4 y 8 en la dirección positiva."

# Extraemos los números del texto
numbers = re.findall(r'-?\d+', text)

# Convertimos los números a enteros
numbers = [int(num) for num in numbers]

# Encontramos la distancia entre las dos partículas más lejanas
distance = max(numbers) - min(numbers)

print("La distancia entre las dos partículas más lejanas es:", distance)

# Ejercicios: Nivel 2

# 1. Escribe un patrón que identifique
# si una cadena es una variable válida en Python.

# Definimos una función que verifica si una cadena es una variable válida en Python


def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_]\w*$'

    if bool(re.match(pattern, variable)):
        return f"La variable {variable} es válida"
    else:
        return f"La variable {variable} no es válida"


# Ejemplos de variables válidas e inválidas
valid_variables = ['my_var', 'myVar', '_my_var', 'myVar123', 'my_var_123']
invalid_variables = ['123myvar', 'my-var', 'my var', 'my$var']

# Verificamos si las variables son válidas o no
for variable in valid_variables:
    print(variable, is_valid_variable(variable))

for variable in invalid_variables:
    print(variable, is_valid_variable(variable))

# Ejercicios: Nivel 3

# 1. Limpia el siguiente texto. Después de limpiarlo, cuenta las tres palabras más frecuentes en la cadena.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Limpiamos el texto
clean_sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)

# Convertimos el texto a minúsculas
clean_sentence = clean_sentence.lower()

# Separamos el texto en palabras
words = clean_sentence.split()

# Creamos un diccionario para contar la frecuencia de cada palabra
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Encontramos las tres palabras más frecuentes
most_freq_words = sorted(word_freq, key=word_freq.get, reverse=True)[:3]

print("Las tres palabras más frecuentes son:", most_freq_words)

# Ejercicios: Nivel 4

# 1. Extrae el DNI de la siguiente cadena.

dni = """Asunto: Datos para la nómina.
Respondiendo a su mail, le paso el dato personal que le faltaba. Mi DNI es 12345678A.
Saludos.
"""

# Extraemos el DNI
dni = re.search(r'\d{8}[A-Z]', dni).group()

print("DNI:", dni)
