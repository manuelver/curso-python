"""
Clases
"""

# La mínima clase es poner pass


class Pajaro:
    pass


# mi_pajaro es una instancia de Pajaro,
# que en este punto se considera un objeto
mi_pajaro = Pajaro()

# Si intentamos mostrar la expresión mínima nos dirá
# que es un objeto guardado en cierto espacio de memoria
print(mi_pajaro)

# Si mostramos el tipo nos dirá __main__
print(type(mi_pajaro))

# Podemos crear más objectos y serán distintos de la misma clase
otro_pajaro = Pajaro()

# Mostrando en pantalla nos mostrará que se guarda
# en otro espacio de memoria
print(otro_pajaro)
