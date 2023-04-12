"""
Módulo math

Contiene el kit completo para trabajar con números:
Matemática clásica y avanzada.

También existe el módulo numpy 
que es más avanzado aún. https://numpy.org/

"""

import math

# EJEMPLOS

# Redondeo hacia abajo, hacia el piso
resultado = math.floor(90.99999)
print(resultado)

# Redondeo hacia arriba, hacia el techo
resultado = math.ceil(90.11111)
print(resultado)

# Mostrar pi
resultado = math.pi
print(resultado)

# Calcular un log, en función de un número
# y una base, saber por cuanto deberíamos exponer
# la base para llegar al número
resultado = math.log(625, 5)
print(resultado)
# Calcular en base 10
resultado = math.log10(25)
print(resultado)

# Calcular la tangente
resultado = math.tan(2565)
print(resultado)

# Calcular la coseno
resultado = math.cos(2565)
print(resultado)

# Calcular la raíz cuadrada de pi
resultado = math.sqrt(math.pi)
print(resultado)

# Calcular factorial
resultado = math.factorial(7)
print(resultado)
