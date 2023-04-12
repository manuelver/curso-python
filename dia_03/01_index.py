
print("# BUSCAR LA POSICIÓN DE UN CARACTER")
# CON index() PODEMOS ENCONTRAR LA POSICIÓN DE UN CARACTER EN UN STRING
mi_texto = "hola mundo"
posicion = mi_texto.index("o",0,11)
print(f"EJEMPLO: La posición del caracter \"o\" es {posicion}")

# PREGUNTAR LETRA Y DAR POSICIÓN EN FRASE
pregunta_carater = input("PREGUNTA: De qué carater quieres saber la posición: ")
print(f"El carater \"{pregunta_carater}\" está en la posición \"{mi_texto.index(pregunta_carater)}\"")

print("\n# SE PUEDE BUSCAR CON rindex PARA BUSCAR DE DERECHA A IZQUIERDA")
posicion_r = mi_texto.rindex("o")
print(f"EJEMPLO: La posición en búsqueda reversa del caracter \"o\" es {posicion_r}")

print("\n# BUSCAR EL CARACTER DE UNA POSICIÓN")
# SABER LA LETRA DE UNA POSICIÓN
que_carater = mi_texto[3]
print(f"EJEMPLO: El carater en la posición \"3\" del string es la \"{que_carater}\"")

# PREGUNTAR POSICIÓN Y DAR RESULTADO EN FRASE
pregunta_posicion = int(input("PREGUNTA: De que posición quieres saber el caracter: "))
resultado_posicion = mi_texto[pregunta_posicion]
print(f"En la posición \"{pregunta_posicion}\" está el caracter \"{resultado_posicion}\"")
