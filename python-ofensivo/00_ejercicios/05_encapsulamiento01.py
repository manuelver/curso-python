#!/usr/bin/env python3
"""
Encapsulamiento y métodos especiales

Hay un convenio que se utiliza en Python para indicar que un atributo 
o método es privado o protegido. No se debería usar fuera de la clase.
Atributo protegido
self._dinero

Atributo privado:
self.__dinero

Esto activa un mecanismo de cambio de nombre conocido como ‘name mangling‘, 
donde el intérprete de Python altera internamente el nombre del atributo 
para hacer más difícil su acceso desde fuera de la clase.

Para extraerlo hay que poner el nombre de la clase delante del atributo
self._Ejemplo__dinero

"""


class Ejemplo:

    def __init__(self):

        # Atributo protegido
        self._atributo_protegido = "Soy un atributo protegido y no deberías poder verme"

        # Atributo privado

        self.__atributo_privado = "Soy un atributo privado, inalcanzable desde fuera de la clase"


ejemplo = Ejemplo()

print(ejemplo._atributo_protegido)  # Acceso al atributo protegido
print(ejemplo._Ejemplo__atributo_privado)  # Acceso al atributo privado
print(ejemplo.__atributo_privado)  # Error
