#!/usr/bin/env python3
"""
Maneras de imprimir una variable
"""

name = "Sergi"
rol = "SysAdmin"

edad = 53

print("Hello, I'm %s your %s of %d years!" % (name, rol, edad))

print("Hello, I'm " + name + " your " + rol + " of " + str(edad) + " years!")

print("Hello, I'm {0} your {1} of {2} years! Yes, {0}".format(name, rol, edad))

# f-strings
print(f"Hello, I'm {name} your {rol} of {edad} years!")
