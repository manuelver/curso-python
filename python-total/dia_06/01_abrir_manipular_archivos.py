"""
Abrir y manipular archivos 
"""
# Abrir documento
archivo = open('prueba.txt')

# Leer todo el documento
archivo_total = archivo.read()

# print(archivo_total)
print(archivo_total)
archivo.close()

print('-'*25)

# Con este método se lee una sola línea
mi_archivo = open('prueba.txt')
una_linea = mi_archivo.readline()

print(una_linea.upper())
print(una_linea)

una_linea = mi_archivo.readline()

# Con el método rstrip no se efectuará salto de línea
print(una_linea.rstrip())
una_linea = mi_archivo.readline()

print(una_linea)
# close cierrar el archivo para no ocupar
# el espacio de memoria que deja abierto en open.
# Es importante usarlo siempre
mi_archivo.close()

print('-'*25)

archivo2 = open('prueba.txt')
# Se puede iterar por líneas
for l in archivo2:
    print('Aquí dice que : ' + l)

archivo2.close()

print('-'*25)

arch = open('prueba.txt')
# Con este método se meten las líneas en una lista.
# Hay que tener en cuenta que estos métodos que cargan
# todo el archivo deben usarse con modelación,
# ya que cargan mucho la memoria sobretodo si son
# ficheros grandes y el mismo muchas veces.
todas = arch.readlines()

print(todas)


arch.close()

print('-'*25)

# Imprimir la segunda linea
txt = open('prueba.txt')

list_txt = txt.readlines()

cuenta_lineas = 0
for l in list_txt:
    cuenta_lineas += 1
    if cuenta_lineas == 2:
        print(l)

print()
txt.close()
