color_auto = 'rojo'
matricula = 266254

print("Mi coche es {} con la matrícula {}".format(color_auto,matricula))

# A partir de la versiuón 3.6 se incorporaron las cadenas literales

print(f"\nMi coche es {color_auto} con la matrícula {matricula}")

# Evolución de format
x = 10
y = 5
z = x + y

print("\nMis números son " + str(x) + " y " + str(y) + " es igual a " + str(z))

print("\nMis números son {} y {} es igual a {}".format(x,y,z))

print(f"\nMis números son {x} y {y} es igual a {z}")

