"""
03_introduccion.py
"""
import math


# Ejemplos de diferentes tipos de datos en Python
entero = 10
flotante = 3.14
complejo = 2 + 3j
cadena = "Hola, mundo!"
booleano = True
lista = [1, 2, 3, "cuatro"]
tupla = (1, 2, 3, "cuatro")
conjunto = {1, 2, 3, 4, 5}
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Imprimiendo los tipos de datos
print(type(entero))
print(type(flotante))
print(type(complejo))
print(type(cadena))
print(type(booleano))
print(type(lista))
print(type(tupla))
print(type(conjunto))
print(type(diccionario))

# Cálculo de la distancia euclidiana

# Define the coordinates of the two points
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Print the result
print("Euclidean distance:", distance)
