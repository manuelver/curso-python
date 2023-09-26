"""
01_modulos.py
"""
import random
import string

# Ejercicios: Nivel 1

# 1. Escribe una función que genere
# un identificador de usuario aleatorio
# de seis dígitos/caracteres.


def random_user_id():
    contra = ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=6))

    return contra


print(random_user_id())

# 2. Modifica la tarea anterior.
# Declara una función llamada user_id_gen_by_user.
# No toma parámetros,
# pero toma dos entradas utilizando input().
# Una de las entradas es el número de caracteres
# y la segunda entrada es el número de IDs
# que se supone que deben generarse.
# ```


def user_id_gen_by_user():
    n = int(input("Ingrese el número de caracteres: "))
    m = int(input("Ingrese el número de IDs a generar: "))
    user_ids = []
    for i in range(m):
        user_id = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=n))
        user_ids.append(user_id.upper())
    return '\n'.join(user_ids)


print(user_id_gen_by_user())


# 3. Escribe una función llamada rgb_color_gen
# que generará colores RGB
# (3 valores que van desde 0 hasta 255 cada uno).

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r},{g},{b})"


print(rgb_color_gen())


# ### Ejercicios: Nivel 2

# 1. Escribe una función llamada
# list_of_hexa_colors que devuelva
# cualquier cantidad de colores hexadecimales
# en una lista (seis números hexadecimales escritos después del #).


def list_of_hexa_colors(n):
    hexa_colors = []
    for i in range(n):
        hexa_color = ''.join([random.choice('0123456789abcdef')
                             for j in range(6)])
        hexa_colors.append(f"#{hexa_color}")
    return hexa_colors


print(list_of_hexa_colors(5))


# 2. Escribe una función llamada
# list_of_rgb_colors que devuelva
# cualquier cantidad de colores RGB
# en una lista.

def list_of_rgb_colors(n):
    rgb_colors = []
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r},{g},{b})")
    return rgb_colors


print(list_of_rgb_colors(5))


# 3. Escribe una función llamada
# generate_colors que pueda generar
# cualquier cantidad de colores
# hexadecimales o RGB.

def generate_colors():
    color_type = input("¿hexa o rgb? ")
    n = int(input("¿Cuántos colores? "))
    colors = []
    if color_type == 'hexa':
        for i in range(n):
            hexa_color = ''.join(
                [random.choice('0123456789abcdef') for j in range(6)])
            colors.append(f"#{hexa_color}")
    elif color_type == 'rgb':
        for i in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f"rgb({r},{g},{b})")
    return colors


print(generate_colors())


# ### Ejercicios: Nivel 3

# 1. Llama a tu función shuffle_list,
# toma una lista como parámetro
# y devuelve una lista mezclada.

def shuffle_list(lst):
    random.shuffle(lst)
    return lst


my_list = list(range(50))
print(shuffle_list(my_list))

# 2. Escribe una función
# que devuelva una matriz
# de siete números aleatorios
# en un rango de 0-9.
# Todos los números deben ser únicos.


def unique_random_numbers():
    numbers = []
    while len(numbers) < 7:
        number = random.randint(0, 9)
        if number not in numbers:
            numbers.append(number)
    return numbers


print(unique_random_numbers())
