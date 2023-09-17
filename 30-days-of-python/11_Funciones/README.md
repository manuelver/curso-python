# Funciones

Documento original en inglés: [Functions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/11_Day_Functions/11_functions.md)

## Ejercicios

# Ejercicios: Nivel 1

1. Declara una función llamada `add_two_numbers`. Toma dos parámetros y devuelve la suma.

2. El área de un círculo se calcula de la siguiente manera: `área = π x r x r`. Escribe una función que calcule `area_of_circle`.

3. Escribe una función llamada `add_all_nums` que tome un número arbitrario de argumentos y sume todos los argumentos. Verifica si todos los elementos de la lista son de tipo numérico. Si no lo son, proporciona un mensaje de retroalimentación razonable.

4. La temperatura en °C se puede convertir a °F utilizando la siguiente fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta de °C a °F, `convert_celsius_to_fahrenheit`.

5. Escribe una función llamada `check_season`. Toma un parámetro de mes y devuelve la estación: Otoño, Invierno, Primavera o Verano.

6. Escribe una función llamada `calculate_slope` que devuelva la pendiente de una ecuación lineal.

7. La ecuación cuadrática se calcula de la siguiente manera: `ax² + bx + c = 0`. Escribe una función que calcule el conjunto de soluciones de una ecuación cuadrática, `solve_quadratic_eqn`.

8. Declara una función llamada `print_list`. Toma una lista como parámetro y imprime cada elemento de la lista.

9. Declara una función llamada `reverse_list`. Toma un arreglo como parámetro y devuelve el arreglo invertido (usa bucles).

```
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
```

10. Declara una función llamada `capitalize_list_items`. Toma una lista como parámetro y devuelve una lista de elementos en mayúsculas.

11. Declara una función llamada `add_item`. Toma una lista y un parámetro de elemento. Devuelve una lista con el elemento agregado al final.
```
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
```

12. Declara una función llamada `remove_item`. Toma una lista y un parámetro de elemento. Devuelve una lista con el elemento eliminado de ella.
```
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Declara una función llamada `sum_of_numbers`. Toma un número como parámetro y suma todos los números en ese rango.
```
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
```

14. Declara una función llamada `sum_of_odds`. Toma un número como parámetro y suma todos los números impares en ese rango.

15. Declara una función llamada `sum_of_even`. Toma un número como parámetro y suma todos los números pares en ese rango.

## Ejercicios: Nivel 2

1. Declara una función llamada `evens_and_odds`. Toma un número entero positivo como parámetro y cuenta el número de pares e impares en ese número.
```
print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.
```

2. Llama a tu función `factorial`, toma un número entero como parámetro y devuelve el factorial de ese número.

3. Llama a tu función `is_empty`, toma un parámetro y verifica si está vacío o no.

4. Escribe diferentes funciones que tomen listas. Deben calcular la media, mediana, moda, rango, varianza y desviación estándar. Las funciones se llaman `calculate_mean`, `calculate_median`, `calculate_mode`, `calculate_range`, `calculate_variance` y `calculate_std` (desviación estándar).

## Ejercicios: Nivel 3

1. Escribe una función llamada `is_prime` que compruebe si un número es primo.

2. Escribe una función que compruebe si todos los elementos de una lista son únicos.

3. Escribe una función que compruebe si todos los elementos de una lista son del mismo tipo de dato.

4. Escribe una función que compruebe si una variable proporcionada es una variable válida en Python.

5. Ve a la carpeta de datos y accede al archivo countries-data.py.

 - Crea una función llamada `most_spoken_languages_in_the_world`. Debe devolver las 10 o 20 lenguas más habladas en el mundo en orden descendente.

 - Crea una función llamada `most_populated_countries`. Debe devolver los 10 o 20 países más poblados en orden descendente.
