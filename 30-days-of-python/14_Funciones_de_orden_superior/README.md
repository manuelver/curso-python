# Funciones de Orden Superior

Documento original en inglés: [Higher Order Functions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md)

## Ejercicios

```
countries = ['Estonia', 'Finlandia', 'Suecia', 'Dinamarca', 'Noruega', 'Islandia']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Ejercicios: Nivel 1

1. Explica la diferencia entre map, filter y reduce.
2. Explica la diferencia entre función de orden superior, cierre y decorador.
3. Define una función de llamada antes de map, filter o reduce, mira los ejemplos.
4. Usa un bucle for para imprimir cada país en la lista de países.
5. Usa un bucle for para imprimir cada nombre en la lista de nombres.
6. Usa un bucle for para imprimir cada número en la lista de números.

[Solución](01_func_sup.py)

### Ejercicios: Nivel 2

1. Usa map para crear una nueva lista cambiando cada país a mayúsculas en la lista de países.
2. Usa map para crear una nueva lista cambiando cada número por su cuadrado en la lista de números.
3. Usa map para cambiar cada nombre a mayúsculas en la lista de nombres.
4. Usa filter para filtrar los países que contengan 'land'.
5. Usa filter para filtrar los países que tengan exactamente seis caracteres.
6. Usa filter para filtrar los países que contengan seis letras o más en la lista de países.
7. Usa filter para filtrar los países que comiencen con 'E'.
8. Encadena dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback)).
9. Declara una función llamada get_string_lists que tome una lista como parámetro y luego devuelva una lista que contenga solo elementos de tipo cadena.
10. Usa reduce para sumar todos los números en la lista de números.
11. Usa reduce para concatenar todos los países y producir la siguiente oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
12. Declara una función llamada categorize_countries que devuelva una lista de países con algún patrón común (puedes encontrar la [lista de países](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) en este repositorio como countries.js(eg 'land', 'ia', 'island', 'stan')).
13. Crea una función que devuelva un diccionario, donde las claves sean las letras iniciales de los países y los valores sean la cantidad de nombres de países que comienzan con esa letra.
14. Declara una función llamada get_first_ten_countries que devuelva una lista de los primeros diez países de la lista de países.
15. Declara una función llamada get_last_ten_countries que devuelva los últimos diez países en la lista de países.

[Solución](02_func_sup.py)

### Ejercicios: Nivel 3

1. Usa el archivo [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) y sigue las siguientes tareas:
- Ordena los países por nombre, capital y población.
- Filtra los diez idiomas más hablados por ubicación.
- Filtra los diez países más poblados.

[Solución](03_func_sup.py)

[<< Day 13](../13_Comprensión_de_listas/README.md) | [Day 15 >>](../15_Errores_de_tipo_en_Python/README.md)
