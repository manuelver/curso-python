#!/usr/bin/env python3
"""
__Colecciones y estructuras de datos de Python__
Proyecto sumario de ventas y stock de juegos
"""

# Juegos
juegos = [
    "Super Mario Bros", 
    "Zelda", 
    "Cyberpunk 2077", 
    "Final Fantasy"
]

# Géneros
generos = {
    "Super Mario Bros": "Aventuras",
    "Zelda": "Aventuras",
    "Cyberpunk 2077": "RPG",
    "Final Fantasy": "RPG"
}

# Ventas y Stock
ventas_stock = {
    "Super Mario Bros": (
        100, 
        50
    ),
    "Zelda": (
        50, 
        25
    ),
    "Cyberpunk 2077": (
        1000, 
        500
    ),
    "Final Fantasy": (
        500, 
        250
    )
}

# Clientes
clientes = {
    "Super Mario Bros": {
        "Sergi", 
        "Jose", 
        "Maria"
    },
    "Zelda": {
        "Sergi", 
        "Ramón", 
        "Jesus"
    },
    "Cyberpunk 2077": {
        "Fernando", 
        "Jose", 
        "Maria"
    },
    "Final Fantasy": {
        "Eduardo", 
        "Jose", 
        "Maria"
    }
}


# Sumario
def sumario(juego):
    print(f"[{juegos.index(juego) + 1}] {juego}")
    print(f"\t[+] Género: {generos[juego]}")
    print(f"\t[+] Ventas: {ventas_stock[juego][0]} unidades")
    print(f"\t[+] Stock: {ventas_stock[juego][1]} unidades")
    print(f"\t[+] Clientes totales: {len(clientes[juego])}")
    print(f"\t[+] Nombre de clientes: {', '.join(clientes[juego])}")
    print()

print("Sumario de TODOS los juegos")
for juego in juegos:
    sumario(juego)


print("Sumario de los 2 juegos con MÁS STOCK")
for juego in sorted(ventas_stock, key=lambda x: ventas_stock[x][1], reverse=True)[:2]:
    sumario(juego)

ventas_totales = lambda: sum(ventas for ventas, _ in ventas_stock.values())

print("DATOS TOTALES")
print(f"Total de juegos: {len(juegos)}")
print(f"Total de ventas: {ventas_totales()} unidades")
print(f"Total de stock: {sum([ventas_stock[juego][1] for juego in ventas_stock])} unidades")
