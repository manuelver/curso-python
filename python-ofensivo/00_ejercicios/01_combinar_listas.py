#!/usr/bin/env python3
"""
Combinar listas
"""

# Ejercicio 1
odd_number = [1, 3, 5, 7, 9]
even_number = [2, 4, 6, 8, 10]

zip_numbers = zip(odd_number, even_number)

new_list = []
for odd, even in zip_numbers:
    new_list.append(odd + even)

print(new_list)

# Ejercicio 2
odd_number = [1, 3, 5, 7, 9]
even_number = [2, 4, 6, 8, 10]

result = list(map(sum, zip(odd_number, even_number)))

print(result)
