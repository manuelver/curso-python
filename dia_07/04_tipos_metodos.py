"""
Tipos de métodos

# Decoradores:
- Métodos de instancia:

    def mi_metodo(self):
        print('algo')
    mi_metodo

    - Acceden y modifican atributos del objeto.
    - Acceden a otro métodos.
    - Pueden modificar el estado de la clase.

- Métodos de clase      @classmethod:

    def mi_metodo(cls):
        print('algo')

    - No están asociados a las instancias de la clase, sino a la clase en si misma
    - Pueden ser llamados desde la instancia y desde la clase
    - No pueden acceder a los atributos de instancia pero si a los de la clase

- Métodos estáticos     @staticmethod:

    @staticmethod
    def mi_metodo():
        print('algo')

    - No acepta como parámetro ni self ni cls
    - No pueden modificar ni el estado de la clase ni de la instancia
    - Pueden aceptar parámetros de entrada
"""


class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Cuando se hace referencia a un atributo se debe poner self por delante
    # para que se asocie correctamente
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        # De instancia - Acceden a otro métodos
        self.piar()

    # De instancia - Acceden y modifican atributos del objeto
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pájaro es {self.color}')

    # Métodos de clase. Necesita el decorador
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        # No pueden acceder a los métodos de instancia
        # print(f'Es de color {self.color}')
        # Pero si que puede acceder a los métodos de clase
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        # No accede ni a métodos de instancia ni de clase
        # self.color = 'rojo'
        # cls.alas = 2
        # Así te aseguras que no se modifiquen los métodos
        print('El pajaro mira')


Pajaro.poner_huevos(3)

Pajaro.mirar()

piolin = Pajaro('amarillo', 'canario')

piolin.pintar_negro()

piolin.volar(45)

# De instancia - Pueden modificar el estado de la clase
piolin.alas = False
print(piolin.alas)
