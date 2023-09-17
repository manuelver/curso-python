# Comprensión de listas

Documento original en inglés: [List comprehension](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md)

## Ejercicios

### Ejercicios: Nivel 1

1. Filtra solo los números negativos y cero en la lista usando una comprensión de lista.

```python
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
```

2. Aplana la siguiente lista de listas de listas a una lista unidimensional:

```
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

3. Usando una comprensión de lista, crea la siguiente lista de tuplas:

```
[(0, 1, 0, 0, 0, 0, 0),
 (1, 1, 1, 1, 1, 1, 1),
 (2, 1, 2, 4, 8, 16, 32),
 (3, 1, 3, 9, 27, 81, 243),
 (4, 1, 4, 16, 64, 256, 1024),
 (5, 1, 5, 25, 125, 625, 3125),
 (6, 1, 6, 36, 216, 1296, 7776),
 (7, 1, 7, 49, 343, 2401, 16807),
 (8, 1, 8, 64, 512, 4096, 32768),
 (9, 1, 9, 81, 729, 6561, 59049),
 (10, 1, 10, 100, 1000, 10000, 100000)]
```

4. Aplana la siguiente lista a una nueva lista:

```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Resultado:
[['FINLAND', 'FIN', 'HELSINKI'],
 ['SWEDEN', 'SWE', 'STOCKHOLM'],
 ['NORWAY', 'NOR', 'OSLO']]
```
5. Cambia la siguiente lista a una lista de diccionarios:
```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Resultado:
[{'country': 'Finland', 'city': 'Helsinki'},
 {'country': 'Sweden', 'city': 'Stockholm'},
 {'country': 'Norway', 'city': 'Oslo'}]
```
6. Cambia la siguiente lista de listas a una lista de cadenas concatenadas:
```
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# Resultado: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
```
7. Escribe una función lambda que pueda resolver una pendiente o una ordenada al origen de funciones lineales.
