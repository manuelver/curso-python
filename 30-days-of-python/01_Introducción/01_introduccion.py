"""
01_introduccion.py
"""

import platform

# Comprobando la versión de Python
print("Versión de Python:", platform.python_version())

# Operaciones aritméticas
# Variables
a = 3
b = 4

# Operaciones
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Módulo:", b % a)
print("División:", b / a)
print("Potenciación:", a ** b)
print("División entera:", b // a)

# Información personal
nombre = "Romero"
apellido = "Madero"
pais = "Tu país"
print(nombre)
print(apellido)
print(pais)
print("Estoy disfrutando de 30 días de Python")

# Comprobando tipos de datos
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finlandia']))
print(type(nombre))
print(type(apellido))
print(type(pais))
