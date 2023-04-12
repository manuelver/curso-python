"""
Herencia

D ONT'T
R EPEAT
Y OURSELF

No repitas el código!

"""

# Ejemplo


class Animal:

    # Atributos
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    # Métodos
    def nacer(self):
        print("Este animal ha nacido")

    def morir(self):
        pass

    def respirar(self):
        pass


class Pajaro(Animal):
    pass


class Mamifero(Animal):
    pass


class Insecto(Animal):
    pass


# Podemos ver de donde vienen las clase con __bases__
print(Pajaro.__bases__)

# Podemos ver las subclases de una clase
print(Animal.__subclasses__())

# Creamos una instancia de pájaro y debe tener los atributos de Animal
piolin = Pajaro(2, "negro")

print(f'Piolin tiene {piolin.edad} años y es de color {piolin.color}')

# La instancia de Pájaro ha heredado los métodos de Animal
piolin.nacer()
