"""
Compresión de listas
"""

# Las compresión de listas susituye el siguiente ejemplo
lista = []

palabra = "python"

for letra in palabra:
    lista.append(letra)

print(lista)

# Con una sintaxis más breve, de 4 a 1 linea
lista_comp = [letra for letra in "python"]

print(lista_comp)

# Ejemplo con operación
lista_num = [n /2 for n in range(0,21,2)]

print(lista_num)

# Ejemplo con condicional para agregar en la lista
lista_condici = [n for n in range(0,21,2) if n * 2 > 10]

print(lista_condici)

# Ejemplo anterior pero con else. Ahora es menos legible 
# porque hay que ponerlo delante
# Lo que hacemos es sustituir el n por un texto
lista_else = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]

print(lista_else)


# Ejemplo práctico
## Transformar pies en metros

pies = [10,20,30,40,50]

metros = []
for pie in pies:
    metros.append(pie*3.281)
print(metros)

## Ahora la compresión del código
metros_compr = [pie*3.281 for pie in pies]
    
print(metros_compr)

# Valores cuadrados
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrados = [v**2 for v in valores]

print(valores_cuadrados)

# Guardar pares en la lista
valores_pares = [v for v in valores if (v%2 == 0)]
print(valores_pares)

# De fahrenheit a celsius

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(grados_fahrenheit-32)*(5/9) for grados_fahrenheit in temperatura_fahrenheit]

print(grados_celsius)
