""" Intenger & float """

# La suma convierte el int en un float, para poder operar
mi_numero = 5 + 5.8
mi_numero = mi_numero + mi_numero

print(mi_numero)

print(mi_numero + mi_numero)

print(type(mi_numero))

# Cuando pedimos un numero recogemos un string
edad = input("Dime tu edad: ")
print("Tu edad es " + edad)
print(type(edad))

# Por eso tenemos que aplicar una conversión si queremos operar
op_edad = int(edad)
print(type(op_edad))
nueva_edad = 1 + op_edad

# Y si queremos volver a implimir concatenando, debemos transformarlo de nuevo
wr_nueva_edad = str(nueva_edad)
print("Cumpliras " + wr_nueva_edad)

print(type(wr_nueva_edad))
