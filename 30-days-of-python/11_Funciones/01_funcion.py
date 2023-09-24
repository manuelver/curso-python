"""
01_funcion.py
"""
import math

# Ejercicios: Nivel 1

# 1. Declara una función llamada add_two_numbers.
# Toma dos parámetros y devuelve la suma.


def add_two_numbers(a, b):
    return a + b


print(f"La suma de los parámetros es igual a {add_two_numbers(2, 3)}")

# 2. El área de un círculo se calcula de la siguiente manera:
# área = π x r x r.
# Escribe una función que calcule area_of_circle.


def area_of_circle(r):
    return math.pi * r * r


radio = 5
print(
    f"El área del círculo con el radio {radio} es igual a {area_of_circle(radio)}")


# 3. Escribe una función llamada add_all_nums que tome
# un número arbitrario de argumentos y sume todos los argumentos.
# Verifica si todos los elementos de la lista son de tipo numérico.
# Si no lo son, proporciona un mensaje de retroalimentación razonable.


def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num

        else:
            return "No todos los elementos son numéricos"
    return f"La suma de los parámetros es igual a {total}"


print(f"{add_all_nums(1, 2, 3, 4, '5')}")

# 4. La temperatura en °C se puede convertir a °F
# utilizando la siguiente fórmula:
# °F = (°C x 9/5) + 32.
# Escribe una función que convierta de °C a °F,
# convert_celsius_to_fahrenheit.


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatura = 36
print(
    f"La temperatura de {temperatura} °C en fahrenheit es igual a {convert_celsius_to_fahrenheit(temperatura)}")

# 5. Escribe una función llamada check_season.
# Toma un parámetro de mes y devuelve la estación:
# Otoño, Invierno, Primavera o Verano.


def check_season(month):
    if month in [12, 1, 2]:
        return "Invierno"
    elif month in [3, 4, 5]:
        return "Primavera"
    elif month in [6, 7, 8]:
        return "Verano"
    elif month in [9, 10, 11]:
        return "Otoño"
    else:
        return "Mes no válido"


mes = 1
print(f"El mes {mes} es de {check_season(mes)}")

# 6. Escribe una función llamada calculate_slope
# que devuelva la pendiente de una ecuación lineal.


def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


print(
    f"La pendiente de la ecuación lineal es igual a {calculate_slope(2, 3, 6, 7)}")

# 7. La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0.
# Escribe una función que calcule el conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn.


def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x1 = -b / (2*a)
        return (x1,)
    else:
        return "No hay soluciones reales"


print(
    f"Las soluciones de la ecuación cuadrática son {solve_quadratic_eqn(5, 8, 1)}")

# 8. Declara una función llamada print_list.
# Toma una lista como parámetro
# y imprime cada elemento de la lista.


def print_list(my_list):
    for item in my_list:
        print(f" - {item}")


lista_frutas = ["Manzana", "Pera", "Naranja", "Plátano", "Kiwi"]
print_list(lista_frutas)

# 9. Declara una función llamada reverse_list.
# Toma un arreglo como parámetro
# y devuelve el arreglo invertido (usa bucles).


def reverse_list(my_list):
    reversed_list = []
    i = len(my_list) - 1
    while i >= 0:
        reversed_list.append(my_list[i])
        i -= 1
    return reversed_list


lista_numeros = [1, 2, 3, 4, 5]
lista_letras = ["A", "B", "C"]
print(reverse_list(lista_numeros))
print(reverse_list(lista_letras))


# 10. Declara una función llamada
# capitalize_list_items.
# Toma una lista como parámetro
# y devuelve una lista de elementos en mayúsculas.


def capitalize_list_items(my_list):
    return [item.upper() for item in my_list]


print(capitalize_list_items(lista_frutas))

# 11. Declara una función llamada add_item.
# Toma una lista y un parámetro de elemento.
# Devuelve una lista con el elemento agregado al final.


def add_item(my_list, item):
    my_list.append(item)
    return my_list


print(add_item(lista_frutas, "Melón"))
print(add_item(lista_numeros, 6))

# 12. Declara una función llamada remove_item.
# Toma una lista y un parámetro de elemento.
# Devuelve una lista con el elemento eliminado de ella.


def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list


print(remove_item(lista_frutas, "Pera"))
print(remove_item(lista_numeros, 2))

# 13. Declara una función llamada sum_of_numbers.
# Toma un número como parámetro
# y suma todos los números en ese rango.


def sum_of_numbers(n):
    return sum(range(1, n+1))


print(sum_of_numbers(7))

# 14. Declara una función llamada sum_of_odds.
# Toma un número como parámetro
# y suma todos los números impares en ese rango.


def sum_of_odds(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i
    return sum


print(sum_of_odds(7))


# 15. Declara una función llamada sum_of_even.
# Toma un número como parámetro
# y suma todos los números pares en ese rango.


def sum_of_even(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return sum


print(sum_of_even(7))
