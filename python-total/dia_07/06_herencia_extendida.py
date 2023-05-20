"""
Herencia Extendidad

D ONT'T
R EPEAT
Y OURSELF

No repitas el código!

"""


class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f'El pájaro vuela {metros} metros')


# Declarar variables
piolin = Pajaro(3, 'amarillo', 500)

mi_animal = Animal(19, 'negro')

piolin.hablar()

piolin.volar(100)

mi_animal.hablar()

# otro ejemplo


class Padre:
    def hablar(self):
        print('Hola')


class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print('Que tal')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass

# Nieto es capaz de hablar y reir aunque no herede directamente


mi_nieto = Nieto()

mi_nieto.reir()

# El método que hereda es el primero que se encuentra en sus atributos
mi_nieto.hablar()

# Podemos ver el orden de las herencias con __mro__

print(Nieto.__mro__)
