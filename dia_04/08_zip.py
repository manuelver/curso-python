"""
Zip
"""

nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42,55]
ciudades = ['Lima','Madrid','Mexico']

# Cuidao, zip guarda las listas con el numero mínimo de las listas

combinados = list(zip(nombres,edades, ciudades))

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')
