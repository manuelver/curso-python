"""
Ejemplo de función 
"""

# Para desempacar tuples sin funciones
# por ejemplo, para saber el costo de los precios

precios_cafe = [('capuchino',1.5),('expresso',2.2),('moka',1.9)]

for cafe,precio in precios_cafe:
    print(precio * 0.45)

# Pero para saber cual es el café mas caro no nos sirve
# Debemos usar una función:
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return(cafe_mas_caro, precio_mayor)

## Podemos extraer las variables que retorna la función

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El café más caro es {cafe} con un precio de {precio}")


