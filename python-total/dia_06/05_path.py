"""
path
"""

# Ruta relativa

from pathlib import Path

guia = Path("Barcelona", "Sagrada_Familia.txt")

print(guia)

print("-"*25)
# Ruta absoluta al directorio de usuario activo

base = Path.home()
# Con lo cual, si lo unimos a la ruta relativa
# nos dará una ruta absoluta
# (siguiento el path que le hemos dado)
# Admite cadenas como objetos de path
# podemos concatenar varios trozos de paths

mi_ruta = Path('Documents/projectes/python/python_total/dia_06')
guia2 = Path(base, mi_ruta, "Europa", "España", Path(
    "Barcelona", "Sagrada_Familia.txt"))

print(base)
print(guia2)

print("-"*25)
# Utilizando la ruta absoluta anterior,
# podemos cambiar el fichero de destino
guia3 = guia2.with_name("La_Pedrera.txt")

print(guia3)

print("-"*25)
# Acceder a directorios intermedios
# con parent accedemos al path superior cada vez que lo usamos
# Igual que los dos puntos en cd. (..)

print(guia2.parent.parent.parent)

print("-"*25)
# Enumerar todos los archivos txt
# # Primero hacemos la ruta
guia4 = Path(base, mi_ruta, "Europa")

# # Con el método glob recorremos cada objeto de la ruta
# # con un for
for txt in Path(guia4).glob("*.txt"):
    print(txt)

print("-"*25)
# # Recursivo o_O
for txt in Path(guia4).glob("**/*.txt"):
    print(txt)

print("-"*25)
# Para acceder a rutas relativas a partir de una base de rutas absolutas
guia5 = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")

en_europa = guia5.relative_to("Europa")
en_espania = guia5.relative_to("Europa", "España")
print(en_europa)
print(en_espania)
