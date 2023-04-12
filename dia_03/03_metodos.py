""" Métodos en strings """

texto = "Este es el texto de Federico"

# Mayúsculas
resultado01 = texto.upper()
print(resultado01)

# Mayúsculas (Podemos determinar un índice)
resultado02 = texto[20].upper()
print(resultado02)

# Mayúsculas
resultado03 = texto.upper()
print(resultado03)

# Split (Separar dentro de una lista)
resultado04 = texto.split()
print(resultado04)

# Split (Separar dentro de una lista) Se puede seleccionar el elemento separador
resultado05 = texto.split(" ")
print(resultado05)

# Join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
unir = "-".join([a,b,c,d])
print(unir)

# Find
resultado06 = texto.find("F")
print(resultado06)

## La diferencia de find con index es que
## si buscas un carácter que no existe no da error
## arroja el valor -1
resultado07 = texto.find("g")
print(resultado07)

# Reemplazar
resultado08 = texto.replace("Federico", "Manuel")
print(resultado08)


frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

resultado001 = frase.replace("difícil","fácil")
resultado002 = resultado001.replace("mala","buena")

print(resultado002)
