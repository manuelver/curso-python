num1 = 20
num2 = 30.5

# Aquí num1 sigue siendo int
print(num1)
print(type(num1))
print(type(num2))

# Pero con una operación
num1 = num1 + num2

# Transformamos el tipo de num1 a float con una conversión """implícita""" de python
print(num1)
print(type(num1))
print(type(num2))

# Ahora vamos a hacer una conversión explícita
num3 = 5.8
print(num3)
print(type(num3))

# Aquí surge la conversión explícita
num4 = int(num3)

print(num4)
print(type(num4))

# Interesante el ejercicio de convertir str en floar dentro de un print
num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))