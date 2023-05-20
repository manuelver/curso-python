"""
Ejemplos de bucles for
"""

nombres = ['Juan','Ana','Carlos','Belén','Fran']

for nombre in nombres:
    print(f"Hola {nombre}")

print("")

lista = ['a','b','c','d']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

print("")

for nombre in nombres:
    if nombre.startswith('B'):
        print(f"Hola {nombre}")

print("")

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero
    print(mi_valor)
print(f"Total ha sumado {mi_valor}")
print("")

# Si el numero de valores dentro de listas anidadas coincide
# se puede extraer su contenido buscando dos variables.
for i,j in [[1,2],['a','b'],[3,4]]:
    print(i)
    print(j)

print("")

# Diccionario

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}

for item in dic:
    print(item)
print("")

for item in dic.items():
    print(item)
print("")

for item in dic.values():
    print(item)
print("")

for a,b in dic.items():
    print(a)
    print(b)
print("")

# Ejercicio bonito de separar la suma de números de una lista
# por pares e impares

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero

print(suma_pares)
print(suma_impares)


