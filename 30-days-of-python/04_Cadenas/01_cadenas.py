"""
01_cadenas.py
"""

# 1. Concatenando cadenas
cadena_uno = 'Thirty'
cadena_dos = 'Days'
cadena_tres = 'Of'
cadena_cuatro = 'Python'
cadena_completa = cadena_uno + ' ' + cadena_dos + \
    ' ' + cadena_tres + ' ' + cadena_cuatro
print(cadena_completa)

# 2. Concatenando cadenas
cadena_uno = 'Coding'
cadena_dos = 'For'
cadena_tres = 'All'
cadena_completa = cadena_uno + ' ' + cadena_dos + ' ' + cadena_tres
print(cadena_completa)

# 3. Declarando una variable
company = 'Coding For All'

# 4. Imprimiendo la variable
print(company)

# 5. Imprimiendo la longitud de la cadena
print(len(company))

# 6. Cambiando a mayúsculas
print(company.upper())

# 7. Cambiando a minúsculas
print(company.lower())

# 8. Formateando la cadena
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cortando la primera palabra
primera_palabra = company.split()[0]
print(primera_palabra)

# 10. Buscando la palabra 'Coding'
if 'Coding' in company:
    print('La cadena contiene la palabra "Coding"')
else:
    print('La cadena no contiene la palabra "Coding"')

# 11. Reemplazando la palabra 'coding' por 'Python'
nueva_cadena = company.replace('Coding', 'Python')
print(nueva_cadena)

# 12. Cambiando 'Python for Everyone' a 'Python for All'
nueva_cadena = 'Python for Everyone'.replace('Everyone', 'All')
print(nueva_cadena)

# 13. Dividiendo la cadena
cadena_dividida = company.split()
print(cadena_dividida)

# 14. Dividiendo la cadena por coma
cadena_coma = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
cadena_dividida = cadena_coma.split(',')
print(cadena_dividida)

# 15. Carácter en el índice 0
print(company[0])

# 16. Último índice
print(company[-1])

# 17. Carácter en el índice 10
print(company[10])

# 18. Acrónimo para 'Python For Everyone'
acronimo = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(acronimo)

# 19. Acrónimo para 'Coding For All'
acronimo = ''.join([word[0] for word in 'Coding For All'.split()])
print(acronimo)

# 20. Posición de la primera aparición de 'C'
print(company.index('C'))

# 21. Posición de la primera aparición de 'F'
print(company.index('F'))

# 22. Posición de la última aparición de 'l'
print(company.rfind('l'))

# 23. Posición de la primera aparición de 'because'
frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.index('because'))

# 24. Posición de la última aparición de 'because'
print(frase.rindex('because'))

# 25. Cortando la frase 'because because because'
frase_cortada = frase[31:47]
print(frase_cortada)

# 26. Posición de la primera aparición de 'because'
print(frase.index('because'))

# 27. Cortando la frase 'because because because'
frase_cortada = frase[31:47]
print(frase_cortada)

# 28. ¿Empieza 'Coding For All' con un subconjunto 'Coding'?
print('Coding For All'.startswith('Coding'))

# 29. ¿Termina 'Coding For All' con un subconjunto 'coding'?
print('Coding For All'.endswith('coding'))

# 30. Eliminando espacios en blanco
cadena = '  Coding For All   '
cadena_sin_espacios = cadena.strip()
print(cadena_sin_espacios)

# 31. ¿Cuál de las siguientes variables devuelve True cuando usamos el método `isidentifier()`?
#     - 30DaysOfPython
#     - thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32. Uniendo una lista con un hash y espacio
bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
cadena_unida = ' # '.join(bibliotecas)
print(cadena_unida)

# 33. Usando la secuencia de escape de nueva línea
print('Estoy disfrutando de este desafío.\nMe pregunto qué sigue.')

# 34. Usando la secuencia de escape de tabulación
print('Nombre\t\tEdad\t\tPaís\t\tCiudad\nAsab\t\t25\t\tPortugal\tLisboa')

# 35. Usando el método de formato de cadena
radio = 10
area = 3.14 * radio ** 2
print(
    f"El área de un círculo con radio {radio} es de {area} metros cuadrados.")

# 36. Usando métodos de formato de cadena
print(f"8 + 6 = {8+6}")
print(f"8 - 6 = {8-6}")
print(f"8 * 6 = {8*6}")
print(f"8 / 6 = {8/6:.2f}")
print(f"8 % 6 = {8%6}")
print(f"8 // 6 = {8//6}")
print(f"8 ** 6 = {8**6}")
