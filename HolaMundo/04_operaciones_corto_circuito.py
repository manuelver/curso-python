"""
Operaciones de corto circuito
"""

gas = False
encendido = True
edad = 18

# La lectura de las evaluaciones se efectúa de izquierda a derecha
# Con lo cual, cuando tenemos varios "and",
# en el momento que python encuentre un False
# python dejará de leer.
if not gas and encendido and edad >17:
    print("Puedes avanzar")

# En cambio con or, python deja de leer cuando encuentra un True
if not gas or encendido or edad >17:
    print("Puedes avanzar")
