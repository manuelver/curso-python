"""
Polimorfismo

Distintas clases pueden tener el mismo método
pero se aplicará de manera distinta para cada clase
"""


class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Jacinta')

# Dos classes distintas con el mismo método
# que dicen cosas distintas
vaca1.hablar()
oveja1.hablar()


print()
# Ahora en una lista para iterar
# Cuidao! Es genial!
animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()

print()
# También en funciones.
# Impresionante!


def animal_habla(animal):

    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)
