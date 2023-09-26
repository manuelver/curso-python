# Módulos

Documento original en inglés: [Modules](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md)

## Ejercicios

### Ejercicios: Nivel 1

1. Escribe una función que genere un identificador de usuario aleatorio de seis dígitos/caracteres.

```python
print(random_user_id())
# '1ee33d'
```

2. Modifica la tarea anterior. Declara una función llamada user_id_gen_by_user. No toma parámetros, pero toma dos entradas utilizando input(). Una de las entradas es el número de caracteres y la segunda entrada es el número de IDs que se supone que deben generarse.
```
print(user_id_gen_by_user())  # Entrada de usuario: 5 5
# Salida:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf

print(user_id_gen_by_user())  # Entrada de usuario: 16 5
# Salida:
# 1GCSgPLMaBAVQZ26
# YD7eFwNQKNs7qXaT
# ycArC5yrRupyG00S
# UbGxOFI7UXSWAyKN
# dIV0SSUTgAdKwStr
```

3. Escribe una función llamada rgb_color_gen que generará colores RGB (3 valores que van desde 0 hasta 255 cada uno).

```
print(rgb_color_gen())
# 'rgb(125,244,255)' - la salida debe estar en esta forma
```

### Ejercicios: Nivel 2
1. Escribe una función llamada list_of_hexa_colors que devuelva cualquier cantidad de colores hexadecimales en una lista (seis números hexadecimales escritos después del #). El sistema numérico hexadecimal está compuesto por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, de la a a la f. Mira el ejercicio 6 para ejemplos de salida.
2. Escribe una función llamada list_of_rgb_colors que devuelva cualquier cantidad de colores RGB en una lista.
3. Escribe una función llamada generate_colors que pueda generar cualquier cantidad de colores hexadecimales o RGB.

```
generate_colors('hexa', 3)
# ['#a3e12f','#03ed55','#eb3d2b'] 

generate_colors('hexa', 1)
# ['#b334ef']

generate_colors('rgb', 3)
# ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']

generate_colors('rgb', 1)
# ['rgb(33,79, 176)']

```

Ejercicios: Nivel 3
1. Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una lista mezclada.
2. Escribe una función que devuelva una matriz de siete números aleatorios en un rango de 0-9. Todos los números deben ser únicos.

[Solución](01_modulos.py)
