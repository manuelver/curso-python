"""
Métodos
"""

# self es un argumento obligatorio
# hace referencia a cada instancia de la clase


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


piolin = Pajaro('amarillo', 'canario')

piolin.piar()

piolin.volar(50)

# Otro ejemplo


class Persona:
    especie = "humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}')

    def cumplir_anios(self, estado_humor):
        print(f'Cumplir {self.edad + 1} años me pone {estado_humor}')


juan = Persona("Juan", 37)
juan.saludar()
juan.cumplir_anios("feliz")


class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


sonar = Alarma()

sonar.postergar(10)
