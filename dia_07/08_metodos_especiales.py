"""
Métodos especiales

Se han visto:
__init__
__mro__
__bases__
__subclasses__

Vamos a ver:
__str__
__len__
"""

mi_lista = [1, 1, 1, 1, 1, 1, 1, 1]

# print(len(mi_lista))


class Objeto:
    pass


mi_objeto = Objeto()
# No se puede aplicar len
#           print(len(mi_objeto))

# Tampoco podemos ver el objeto
#           print(mi_objeto)

# Otro ejemplo


class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # Vamos a modif el comportamiento del método especial __str__
    # cada vez que se llame para mostrar lo que se quiera
    def __str__(self):
        return f'Albun: {self.titulo} de {self.autor}'

    # Comportamiento de len
    def __len__(self):
        return self.canciones

    # Podemos añadir un mensaje cuando usemos la función del
    def __del__(self):
        print("Se ha eliminado el cd")


mi_cd = CD('Pink Floyd', 'The Wall', 24)

# Ahora sí que veremos el return modificado
print(mi_cd)

# También len, hemos modificado su uso para
# que muestre el número de canciones
print(len(mi_cd))

# Podemos eliminar con la función del
del mi_cd
# Si lo intentamos imprimir nos dirá que no existe
#       print(mi_cd)
