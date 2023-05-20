"""
Compresión listas

Sintaxis:
[expresión for item in items]
"""

# extraer solo un elemento. map
usuarios = [['Chanchito', 4], ['Pulga', 5], ['Felipe', 1]]

nombres_usuarios = [n[0] for n in usuarios]

print(nombres_usuarios)

# Filtrando. filter
nombres_usuarios2 = [n for n in usuarios if n[1] > 2]

print(nombres_usuarios2)

# Ambas operaciones anteriores
nombres_usuarios3 = [n[0] for n in usuarios if n[1] > 2]

print(nombres_usuarios3)


"""
Funciones
map y filter

Ya no se usa, pero hay que tenerlo en cuenta por si se encuentra
Es programación funcional
"""

# map
nombres_usuarios4 = list(map(lambda usuario: usuario[0], usuarios))

print(nombres_usuarios4)

# filter

nombres_usuarios5 = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(nombres_usuarios5)
