# DISTINTAS POSIBILIDADES CON Sub-strings. slicing (rebanar)

# Limitando la rebanada
print("# Limitando la rebanada")
texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fragmento01 = texto[2:15]
print(fragmento01)

# Hasta el final
print("# Hasta el final")
fragmento02 = texto[2:]
print(fragmento02)

# Desde el inicio
print("# Desde el inicio")
fragmento03 = texto[:10]
print(fragmento03)

# Con saltos de dos
print("# Con saltos de dos")
fragmento04 = texto[2:15:2]
print(fragmento04)

# Con saltos de tres de prinicipio a fin
print("# Con saltos de tres de prinicipio a fin")
fragmento05 = texto[::3]
print(fragmento05)

# Con saltos de dos desde el final
print("# Con saltos de dos desde el final")
fragmento06 = texto[::-2]
print(fragmento06)