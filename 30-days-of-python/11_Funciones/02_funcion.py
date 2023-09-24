"""
02_funcion.py
"""


# Ejercicios: Nivel 2

# 1. Declara una función llamada evens_and_odds.
# Toma un número entero positivo como parámetro
# y cuenta el número de pares e impares en ese número.


def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"El número de impares es {odds}.\nEl número de pares es {evens}."


print(evens_and_odds(101))

# 2. Llama a tu función factorial,
# toma un número entero como parámetro
# y devuelve el factorial de ese número.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


num_factorial = 5
print(f"El factorial de {num_factorial} es {factorial(num_factorial)}.")

# 3. Llama a tu función is_empty,
# toma un parámetro
# y verifica si está vacío o no.


def is_empty(item):
    if not item:
        return "La variable está vacía."
    else:
        return "La variable no está vacía."


print(is_empty(""))

# 4. Escribe diferentes funciones que tomen listas.
# Deben calcular la media, mediana, moda, rango,
# varianza y desviación estándar.
# Las funciones se llaman calculate_mean,
# calculate_median, calculate_mode,
# calculate_range, calculate_variance
# y calculate_std (desviación estándar).


def calculate_mean(my_list):
    return sum(my_list) / len(my_list)


def calculate_median(my_list):
    sorted_list = sorted(my_list)
    n = len(my_list)
    if n % 2 == 0:
        return (sorted_list[n//2-1] + sorted_list[n//2]) / 2
    else:
        return sorted_list[n//2]


def calculate_mode(my_list):
    freq_dict = {}
    for num in my_list:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    max_freq = max(freq_dict.values())
    mode_list = [num for num, freq in freq_dict.items() if freq == max_freq]
    if len(mode_list) == len(my_list):
        return None
    elif len(mode_list) == 1:
        return mode_list[0]
    else:
        return mode_list


def calculate_range(my_list):
    return max(my_list) - min(my_list)


def calculate_variance(my_list):
    mean = calculate_mean(my_list)
    return sum([(x - mean)**2 for x in my_list]) / (len(my_list) - 1)


def calculate_std(my_list):
    return calculate_variance(my_list) ** 0.5


my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

print(f"""De la lista {my_list} obtenemos:
 - Media: {calculate_mean(my_list)}
 - Mediana: {calculate_median(my_list)}
 - Moda: {calculate_mode(my_list)}
 - Rango: {calculate_range(my_list)}
 - Varianza: {calculate_variance(my_list)}
 - Desviación estándar: {calculate_std(my_list)}
""")
