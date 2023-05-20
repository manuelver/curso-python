"""
booleano
"""

# Creación directa del booleano
var1 = True
var2 = False
print(type(var1))
print(var1)

# Creación indirecta del booleano
numero = 5 > 2+3
print(type(numero))
print(numero)

# Creación explícita
compara = bool(5 != 5+1)
print(compara)

lista = (1, 2, 3, 4)
control = 5 not in lista
print(type(control))
print(control)
