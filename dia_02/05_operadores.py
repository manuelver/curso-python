x = 6
y = 2
z = 7

# Operadores
print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

# División al piso (redondeando)
print(f"\n{z} dividido al piso de {y} es igual a {z//y}")

# Módulo (resto)
print(f"\n{z} modulo de {y} es igual a {z%y}")

# Numero elevado
print(f"\n{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {y} es igual a {x**3}")
# Raiz cuadrada
print(f"\nLa raíz cuadrada de {x} es {x**0.5}")

print("")
# Redondeo (Hace el redondeo al valor entero más próximo)
print(round(100/3))
print(round(12/7,2))

## La raíz cuadrada de antes
print(f"\nLa raíz cuadrada de {x} es {round(x**0.5,3)}")

## Otro ejemplo para ver el tipo. Veremos que el round es un intenger cuando se redondea en la variable
valor = round(95.6666666666666)
print(valor)
print(type(valor))

### Aquí transformamos el float en intenger dentro del print, pero la variable es un float
valor = 95.6666666666666
print(round(valor))
print(type(valor))

### Si ponemos un redondeo de cero será un float
num1 = round(95.666666666666,0)
print(num1)
print(type(num1))
