"""
01_dic.py
"""

# 1. Crea un diccionario vacío llamado `perro`.
perro = {}

# 2. Agrega las claves `nombre`, `color`, `raza`, `patas` y `edad` al diccionario `perro`.
perro['nombre'] = 'Rintintin'
perro['color'] = 'blanco y negro'
perro['raza'] = 'Mestizo'
perro['patas'] = 4
perro['edad'] = 2

# 3. Crea un diccionario llamado `estudiante` y agrega las siguientes claves: `nombre`, `apellido`, `género`, `edad`, `estado civil`, `habilidades`, `país`, `ciudad` y `dirección`.
estudiante = {
    'nombre': 'Armando',
    'apellido': 'Guerra',
    'género': 'Indefinido',
    'edad': 28,
    'estado civil': 'Soltero',
    'habilidades': ['Python', 'JavaScript'],
    'país': 'México',
    'ciudad': 'Ciudad de México',
    'dirección': 'Calle Libertadores, 23 7º 2ª'
}

# 4. Obtiene la longitud del diccionario `estudiante`.
estudiante_length = len(estudiante)
print(f"El diccionario estudiante tiene {estudiante_length} valores")

# 5. Obtiene el valor de `habilidades` y verifica su tipo de dato, que debería ser una lista.
habilidades = estudiante['habilidades']
if type(habilidades) == list:
    print(f'El valor de habilidades es una lista: {type(habilidades)}')

# 6. Modifica los valores de `habilidades` agregando una o dos habilidades más.
estudiante['habilidades'].extend(['HTML', 'CSS'])

# 7. Obtiene las claves del diccionario como una lista.
estudiante_keys = list(estudiante.keys())
print(f'Las claves del diccionario estudiante son: {estudiante_keys}')

# 8. Obtiene los valores del diccionario como una lista.
estudiante_values = list(estudiante.values())
print(f'Los valores del diccionario estudiante son: {estudiante_values}')

# 9. Convierte el diccionario en una lista de tuplas utilizando el método `items()`.
estudiante_items = list(estudiante.items())

# 10. Elimina uno de los elementos del diccionario.
del estudiante['habilidades']

# 11. Elimina uno de los diccionarios por completo.
del perro
