"""
01_variables.py
"""
# Day 2: 30 Days of Python programming

# Declarando variables
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
pais = "España"
ciudad = "Madrid"
edad = 30
año = 2021
esta_casado = True
es_verdadero = False
esta_luz_encendida = True

# Declarando múltiples variables en una sola línea
x, y, z = 10, 20, 30


# Imprimiendo tipos de datos
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(edad))
print(type(pais))
print(type(esta_casado))

# Encontrando la longitud del nombre
longitud_nombre = len(nombre)
print("La longitud de mi nombre es:", longitud_nombre)

# Comparando la longitud del nombre y el apellido
longitud_apellido = len(apellido)
if longitud_nombre > longitud_apellido:
    print("Mi nombre es más largo que mi apellido")
elif longitud_nombre < longitud_apellido:
    print("Mi apellido es más largo que mi nombre")
else:
    print("Mi nombre y mi apellido tienen la misma longitud")

# Realizando operaciones aritméticas
num_uno = 5
num_dos = 4

total = num_uno + num_dos
diferencia = num_uno - num_dos
producto = num_uno * num_dos
division = num_uno / num_dos
resto = num_dos % num_uno
exp = num_uno ** num_dos
division_piso = num_uno // num_dos

print(total)
print(diferencia)
print(producto)
print(division)
print(resto)
print(exp)
print(division_piso)

# Calculando el área y la circunferencia de un círculo
radio = 30
pi = 3.14159

area_de_circulo = pi * radio ** 2
circunferencia_de_circulo = 2 * pi * radio

print(area_de_circulo)
print(circunferencia_de_circulo)

# Obteniendo información del usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
pais = input("Ingresa tu país: ")
edad = input("Ingresa tu edad: ")

# Verificando las palabras clave de Python
help('keywords')
