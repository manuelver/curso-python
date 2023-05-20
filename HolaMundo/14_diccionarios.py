"""
Diccionarios
clave = valor

La clave solo puede ser string.
El valor puede ser cualquier cosa

La clave no se puede modificar.
El valor sí.
"""

punto = {'x': 25, 'y': 50}

print(punto)

# No se puede acceder mediante indice.
# El indice es el strinf de la clave
print(punto['x'])


# Y cuidao, si la llave no existe da error
# Para que no de error es mejor usar un if
if "lala" in punto:
    print(punto["lala"])


# Añadir otra clave y su valor
punto["z"] = 45

print(punto)

# Otro método para obtener valores es get

print(punto.get("y"))

# Con este método no da error si no existe.
# devolverá None
print(punto.get("lala"))

# Y podemos indicar un valor por defecto
# para el caso que no exista
print(punto.get("lala", 97))


# Para eliminar
del punto["x"]
# Función del
del (punto["y"])

print(punto)
