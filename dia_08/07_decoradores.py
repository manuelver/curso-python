"""
Decoradores

Empiezan con @

Son funciones que modifican funciones.


"""


def cambiar_letras(tipo):
    """ 
    Esto sirve para explicar 
    una función dentro de otra
    """
    def mayusculas(text):
        print(text.upper())

    def minusculas(text):
        print(text.lower())

    if tipo == "may":
        return mayusculas
    elif tipo == "min":
        return minusculas


operacion = cambiar_letras('may')

operacion('probando')

# Ahora vamos a crear un decorador


def decorar_saludo(funcion):
    """ Una función con funciones dentro """
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('adios')

    return otra_funcion

# Ahora vamos a crear dos funciones
# una decorada y la otra no


@decorar_saludo
def trabajando(lugar):
    print(f'Estoy trabajando en {lugar}....')


def durmiendo(lugar):
    print(f'Estoy durmiendo en {lugar}')


trabajando("Python")

durmiendo('la cama')


print()

# Ahora vamos a usar el decorador
# directamente en una variable

durmiendo_decorado = decorar_saludo(durmiendo)

durmiendo_decorado('en la playa')
