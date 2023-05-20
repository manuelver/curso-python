"""
Ejemplos de bucle while
"""

contador = 0

while contador < 10:
    contador += 1
    print(f"Iteración número {contador}")

print("Se cumplió la condición")



respuesta = 's'

while respuesta == 's':
    respuesta = input("quieres seguir? (s/n) ")
else:
    print("Gracias")


print("")

# pass      Sirve para reservar un lugar en un bucle, 
# no utilizarlo para recuperar quizá luego

while respuesta == 's':
    pass
print("hola")

print("")

# break         Sirve para romper un bucle y salir
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'D':
        break
    print(letra)

print("")

# continue     Interrumpe la iteración pero no sale, 
# vuelve al inicio de la iteración
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'D':
        continue
    print(letra)



comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)
