"""
Tipos de listas
"""

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
palabras = ['chanchito', 'feliz']
palabras = ['chanchito', 'feliz', 'Felipe', 'alumno']
booleans = [True, False, True, True]
matriz = [[0, 1], [1, 0]]

# tener una lista multiplicada
ceros = [0] * 10
ceros_unos = [0, 1] * 10

# Unir dos listas
alfanumerico = numeros + letras

# Crear un rango de numeros en una lista
rango = list(range(1, 11))

# Crear una lista de un string
chars = list("hola mundo")


"""
Manipulando listas
"""

mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]

# Accediendo a un elemento
print(mascotas[0])

# Cambiar un elemento
mascotas[0] = "Bicho"
print(mascotas)

# Pedir un fragmento de la lista
print(mascotas[2:])
print(mascotas[-1])


"""
Desempaquetar listas
"""

primero, segundo, tercero = numeros

mas_numeros = list(range(1, 11))
primero, *otros = mas_numeros
primero, segundo, *otros, penultimo, ultimo = mas_numeros

print(primero, segundo, otros, penultimo, ultimo)


"""
Acceder al indice de una lista
"""

for mascota in enumerate(mascotas):
    print(mascota)
    # Con la función enumarate nos devuelve tuplas
    # Con lo cual, con 0 nos devuelve el indice
    print(mascota[0])
    # Y con 1 nos devuelve la mascota
    print(mascota[1])

# Entonces, guardamos en el for el indice ya lo tendremos en una variable
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)


"""
Buscar elementos
"""

mascotas.index("Pelusa")
# Pero indice da error si no encuentra el elemento
# mascotas.index("Wolfgang")

# Podemos ingresa un nuevo elemento en la lista indican su indice
mascotas.insert(3, "Pelusa")
# Para agregar al final de la lista
mascotas.append("Mun")

print(mascotas)

# Podemos contar las veces que hay un elemento en una lista con count
print(mascotas.count('Pelusa'))

# Para eliminar. Pero solo elimina la primera vez
mascotas.remove('Pelusa')
print(mascotas)

# Para eliminar el último elemento
mascotas.pop()
print(mascotas)

# Y por su indice
mascotas.pop(1)
print(mascotas)

# También se puede eliminar con del
del mascotas[0]
print(mascotas)

# Para eliminar por completo
mascotas.clear()
print(mascotas)


"""
Ordenando listas
"""

desorden = [2, 1, 44, 23, 66, 34, 78, 5]

# Orden derecho
desorden.sort()
print(desorden)

# Orden inverso
desorden.sort(reverse=True)
print(desorden)

# Con sort() se ordena la lista pero
# Con sorted() nos devolverá una nueva lista
# Entonces, hay que asignarlo a otra lista

nueva_lista = sorted(desorden)

print(nueva_lista)
# La primera lista no se verá afectada
print(desorden)

# A sorted() también se puede hacer el inverso
nueva_lista = sorted(desorden, reverse=True)

# Ordenamos listas dentro de una lista
usuarios = [[4, 'Chanchito'], [5, 'Pulga'], [1, 'Felipe']]

usuarios.sort()
print(usuarios)

# Con en integer segundo ordenad por el primer elemento
usuarios2 = [['Chanchito', 4], ['Pulga', 5], ['Felipe', 1]]
usuarios2.sort()
print(usuarios2)

# Pero podemos indicar que ordene por el segundo elemento "[1]"
# con una función

usuarios3 = [['Chanchito', 4], ['Pulga', 5], ['Felipe', 1]]


def ordena(elemento):
    return elemento[1]


# Con key indicamos que sort() pase los argumentos a la función usuarios3
# y devolverá la lista pero solo del elemento indicado dentro de la función
# Aquí podríamos pasar un segundo argumento como reverse=True
usuarios3.sort(key=ordena)
print(usuarios3)

# Esto se puede hacer más elegante
# con funciones lambda (Funciones canónicas)
# Sintaxis: (key=lambda parámetro:valorRetorno)
# La lambda sustituye a la anterior función ^_^

usuarios3.sort(key=lambda elemento: elemento[1])
