"""
01_operadores.py
"""


# Ejercicios

# 1. Declara tu edad como una variable entera.
edad = 25

# 2. Declara tu altura como una variable de tipo flotante.
altura = 1.80

# 3. Declara una variable que almacene un número complejo.
num_complejo = 3 + 4j

# 4. Escribe un script que solicite al usuario que ingrese la base y la altura de un triángulo y calcule el área de este triángulo (área = 0.5 x b x h).
base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))
area = 0.5 * base * altura
print("El área del triángulo es", area)

# 5. Escribe un script que solicite al usuario que ingrese los lados a, b y c de un triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c).
a = float(input("Ingresa el lado a: "))
b = float(input("Ingresa el lado b: "))
c = float(input("Ingresa el lado c: "))
perimetro = a + b + c
print("El perímetro del triángulo es", perimetro)

# 6. Obtén la longitud y el ancho de un rectángulo utilizando el comando de solicitud (prompt). Calcula su área (área = longitud x ancho) y su perímetro (perímetro = 2 x (longitud + ancho)).
longitud = float(input("Ingresa la longitud: "))
ancho = float(input("Ingresa el ancho: "))
area = longitud * ancho
perimetro = 2 * (longitud + ancho)
print("El área del rectángulo es", area)
print("El perímetro del rectángulo es", perimetro)

# 7. Obten el radio de un círculo utilizando el comando de solicitud (prompt). Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r), donde pi = 3.14.
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.14
area = pi * radio ** 2
circunferencia = 2 * pi * radio
print("El área del círculo es", area)
print("La circunferencia del círculo es", circunferencia)

# 8. Calcula la pendiente, la intersección en el eje x y la intersección en el eje y de la ecuación y = 2x - 2.
pendiente = 2
interseccion_x = 1
interseccion_y = -2

# 9. La pendiente es (m = y2 - y1 / x2 - x1). Calcula la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6, 10).
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La pendiente es", pendiente)
print("La distancia euclidiana es", distancia)

# 10. Compara las pendientes en los ejercicios 8 y 9.
# La pendiente en el ejercicio 8 es igual a la pendiente en el ejercicio 9.

# 11. Calcula el valor de y (y = x^2 + 6x + 9). Intenta usar diferentes valores de x y descubre en qué valor de x y será igual a 0.
lista_de_x = [2, -3, 5, -8]
for x in lista_de_x:
    y = x ** 2 + 6 * x + 9
    print("Si \"x\" es igual a", x, "entonces \"y\" es igual a", y)

# 12. Encuentra la longitud de 'python' y 'dragon' y crea una declaración falsa de comparación.
longitud_python = len("python")
longitud_dragon = len("dragon")
comparacion = longitud_python == longitud_dragon
print("La comparación es", comparacion)

# 13. Utiliza el operador 'and' para verificar si 'on' se encuentra en 'python' y 'dragon'.
en_python = "on" in "python"
en_dragon = "on" in "dragon"
print("Encuentra on en python y dragon: ", en_python and en_dragon)

# 14. Espero que este curso no esté lleno de jerga. Usa el operador 'in' para verificar si 'jerga' está en la oración.
oracion = "Espero que este curso no esté lleno de jerga."
print("Encuentra jerga en la oración:", "jerga" in oracion)

# 15. No hay 'on' ni en dragon ni en python.

# 16. Encuentra la longitud del texto 'python' y convierte el valor a flotante y luego a cadena.
longitud_python = len("python")
longitud_python_flotante = float(longitud_python)
longitud_python_cadena = str(longitud_python_flotante)
print(longitud_python)
print(longitud_python_flotante)
print(longitud_python_cadena)

# 17. Los números pares son divisibles por 2 y el residuo es cero. ¿Cómo puedes verificar si un número es par o no utilizando Python?
numero = 4
es_par = numero % 2 == 0
print("Es par:", es_par)

# 18. Comprueba si la división entera de 7 entre 3 es igual al valor convertido a entero de 2.7.
division_entera = 7 // 3
valor_entero = int(2.7)
comparacion = division_entera == valor_entero
print("Comparación:", comparacion)

# 19. Comprueba si el tipo de '10' es igual al tipo de 10.
tipo_1 = type('10')
tipo_2 = type(10)
comparacion = tipo_1 == tipo_2
print("Comparación:", comparacion)

# 20. Comprueba si int('9.8') es igual a 10.
try:
    valor = int('9.8')
except ValueError:
    valor = None
comparacion = valor == 10
print("Comparación:", comparacion)

# 21. Escribe un script que solicite al usuario que ingrese las horas y la tarifa por hora. Calcula el salario de la persona.
horas = float(input("Ingresa las horas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
salario = horas * tarifa
print("Tus ganancias semanales son", salario)

# 22. Escribe un script en Python que muestre la siguiente tabla.
for i in range(1, 6):
    print(i, 1, i, i ** 2, i ** 3)
