"""
min() y max()
"""

menor = min(56, 96, 72, 63, 35)
print(menor)

mayor = max(56, 96, 72, 63, 35)
print(mayor)

lista = [56, 96, 72, 63, 35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')


# También funciona con strings, alfabéticamente, en listas
nombres = ['Juan', 'Pablo', 'Alicia', 'Carlos']
print(min(nombres))

# y en strings directamente. Buscando primero en las mayúsculas
# y después en las minúsculas
nombre = "Iñigo"
print(max(nombre))


# Y con los diccionarios
dic = {'C1':45,'C2':11}
print(min(dic)) # Esto revisa el diccionario completo
print(min(dic.values()))

