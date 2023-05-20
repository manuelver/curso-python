"""
Atributos
"""


# Sintaxis:
# def tipo/método (tipo_parámetro, parámetro):
#   tipo_parámetro.atributo = parámetro

# Creamos la clase


class Pajaro:
    # Atributos de clase
    # Para valores comunes entre todos los objetos de la clase
    alas = True

    # Atributos de instancia
    # Constructor de la clase pajaro --> Con el método__init__
    def __init__(self, color, especie):  # En el paréntesis pasamos dos parámetros
        self.color = color     # Le damos la instancia que vamos a crear con el atributo
        self.especie = especie


# Creamos la instancia. Si dejamos vacios los paréntesis dará error.
# por que pajaro exige un argumento, debe ser un valor para el atributo.
mi_pajaro = Pajaro('negro', 'Tucan')

# Con el punto podremos ver el atributo entre otras propiedades
print(
    f'Mi pajaro es de color {mi_pajaro.color} y de la especie {mi_pajaro.especie}')

# Los atributos de clases se pueden dar a la clase y a la instancia:
print(Pajaro.alas, mi_pajaro.alas)
