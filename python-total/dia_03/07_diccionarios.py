# DICCIONARIOS (No se puede repetir el valor)
mi_diccionario = {"c1":"valor1","c2":"valor2"}
print(type(mi_diccionario))
print(mi_diccionario)

# Guardando un valor
resultado = mi_diccionario['c1']
print(resultado)

# Ejemplo 1
cliente = {
    'nombre':'Juan',
    'apellido':'Fuentes',
    'peso':'88',
    'talla':'1760'
}
consulta = (cliente['talla'])
print(consulta)

# Ejemplo 2
paciente ={
    "nombre":"Eusebio",
    "apellido":"García",
    "peso":82.6,
    "altura":"172"
}
print(f"El paciente se llama {paciente['nombre']} {paciente['apellido']} pesa {paciente['peso']} kg y mide {paciente['altura']} cm.")

# Diccionarios anidados y listas anidadas
dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3'])
print(dic['c3']['s2'])

# Ejercicio sacar la letra e en mayúscula
diccio = {'c1':['a','b','c'],'c2':['d','e','f']}
print(diccio['c2'][1].upper())

# Cambios en un diccionario
dic2 = {1:'a',2:'b'}
print(dic2)
dic2[3] = 'c'
print(dic2)
dic2[2] = 'B'
print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.items())

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'

print(mi_dic)