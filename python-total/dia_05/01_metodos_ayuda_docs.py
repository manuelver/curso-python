"""
Métodos, ayuda y documentación 
"""

dic = {'clave1': 100, 'clave2': 500}

a = dic.popitem()

print(a)
print(dic)


# Ejercicio 1
exer1 = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#")

print(exer1)


# Ejercicio 2
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3, "naranja")

print(frutas)


# Ejercicio 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)
