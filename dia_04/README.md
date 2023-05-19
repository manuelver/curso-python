# Día 4 - Programa el juego "adivina el número"

## Índice

- [Día 4 - Programa el juego "adivina el número"](dia_04/README.md)
  - [4.1. - Operadores de comparación](dia_04/01_operadores_de_comparacion.md)
  - [4.2. - Operadores lógicos](dia_04/02_operadores_logicos.md)
  - [4.3. - Control de flujo](dia_04/03_control_de_flujo.md)
  - [4.4. - loops while](dia_04/04_loops_while.md)
  - [4.5. - range( )](dia_04/05_range.md)
  - [4.6. - enumerate( )](dia_04/06_enumerate.md)
  - [4.7. - zip( )](dia_04/07_zip.md)
  - [4.8. - min( ) & max( )](dia_04/08_min_max.md)
  - [4.9. - random](dia_04/09_random.md)
  - [4.10. - Comprensión de listas](dia_04/10_comprension_de_listas.md)
  - [4.11. - match](dia_04/11_match.md)
  - [4.12. - Proyecto del Día 4](dia_04/12_proyecto.md)

## 4.1. - Operadores de comparación

Como su nombre lo indica, sirven para comparar dos o más valores. El resultado de esta comparación es un booleano (True/False)

| Operador | Descripción       |
| :------: | :---------------- |
|    ==    | Igual a           |
|    !=    | Diferente a       |
|    >     | Mayor que         |
|    <     | Menor que         |
|    >=    | mayor o igual que |
|    <=    | menor o igual que |

Si la comparación resulta verdadera, devuelve el resultado *True*

Si dicha comparación es falsa, el resultado es *False*
```python
mi_bool = 5 >= 6
print(mi_bool)
```

    False

```python
mi_bool = 5 != 6
print(mi_bool)
```

    True

```python
mi_bool = 10 == 2*5
print(mi_bool)
```

    True

```python
mi_bool = 5 < 6
print(mi_bool)
```

    True


## 4.2. - Operadores lógicos

Estos operadores permiten tomar decisiones basadas en múltiples condiciones.
```python
	a = 6 > 5		
  b = 30 == 15*3
```

**and** 		devuelve True si todas las condiciones son verdaderas
```python
mi_bool = a and b
print(mi_bool)
```

    False

**or**		devuelve True si al menos una condición es verdadera
```python
mi_bool = a or b
print(mi_bool)
```

    True

**not**		devuelve True si el valor del booleano es False, y False si es True
```python
mi_bool = not a
print(mi_bool)
```

    False

## 4.3. - Control de flujo

El control de flujo determina el orden en que el código de un programa se va ejecutando. En Python, el flujo está controlado por estructuras condicionales, loops y funciones.

### 4.3.1. - Estructuras condicionales (if)

- Expresión de resultado booleano (True/False)

- La indentación es obligatoria en Python

- Los dos puntos (:) dan paso al código que se ejecuta si expresión = True
```python
if expresión:
  código a ejecutarse
elif expresión:
  código a ejecutarse
elif expresión:
  código a ejecutarse
...
else:
  código a ejecutarse
```

- *else & elif* son	opcionales  y pueden incluirse varias cláusulas elif

## 4.4. - loops while

Si bien los loops while son otro tipo de bucles, resultan más parecidos a los condicionales if que a los loops for. Podemos pensar a los loops while como una estructura condicional que se ejecuta en repetición, hasta que se convierte en falsa.
```python
while condición:
  expresión
else:
  expresión
```

- Se compone de la Estructura condicional seguida de dos puntos (:)

- La indentación es obligatoria en Python.

- Este código se ejecutará cuando la condición se convierta en False

### 4.4.1. - instrucciones especiales
- Si el código llega a una instrucción break, se produce la salida del bucle.

- La instrucción continue interrumpe la iteración actual dentro del bucle, llevando al programa a la parte superior del bucle.

- La instrucción pass no altera el programa: ocupa un lugar donde se espera una declaración, pero no se desea realizar una acción.

## 4.5. - range( )

La función range( ) devuelve una secuencia de números dados 3 parámetros. Se utiliza fundamentalmente para controlar el número de ejecuciones de un loop o para crear rápidamente una serie de valores.

- *valor_inicio* -		número a partir del cual inicia el rango (incluido)
- *valor_final*	-	número antes del cual el rango finaliza (no incluido)
- *paso*	-		diferencia entre cada valor consecutivo de la secuencia

Sintaxis:
```python
range(valor_inicio, valor_final, paso)
print(list(range(1,13,3)))
```

  [1,4,7,10]

El único parámetro obligatorio es *valor_final*. Los valores predeterminados para *valor_inicio* y *paso* son 0 y 1 respectivamente.
## 4.6. - enumerate( )

La función enumerate( ) nos facilita llevar la cuenta de las iteraciones, a través de un contador de índices de un iterable, que se puede utilizar de manera directa en un loop, o convertirse en una lista de tuplas con el método list( ).

- *iterable* - 		Cualquier objeto que pueda ser iterado
- *inicio* - 			Valor [int] de inicio del índice (por defecto iniciado en 0)

Sintaixs:
```python
enumerate(iterable, inicio)

print(list(enumerate("Hola")))
```

    [(0, 'H'), (1, 'o'), (2, 'l'), (3, 'a')]

```python
for indice, numero in enumerate([5.55, 6, 7.50]):
  print(indice, numero)
```

    0 5.55
    1 6
    2 7.5

## 4.7. - zip( )

La función zip( ) crea un iterador formado por los elementos agrupados del mismo índice provenientes de dos o más iterables. Zip deriva de zipper (cremallera o cierre), de modo que es una analogía muy útil para recordar.

La función se detiene al cuando se agota el iterable con menor cantidad de elementos.
```python
letras = ['w', 'x', 'c']
numeros = [50, 65, 90, 110, 135]
for letra, num in zip(letras, numeros):
  print(f'Letra: {letra}, y Número: {num}')
```

    Letra: w, y Número: 50
    Letra: x, y Número: 65
    Letra: c, y Número: 90

## 4.8. - min( ) & max( )

La función min( ) retorna el item con el valor más bajo dentro de un iterable. La función max( ) funciona del mismo modo, devolviendo el valor más alto del iterable. Si el iterable contiene strings, la comparación se realiza alfabéticamente. 
```python
ciudades_habitantes = {"Tijuana":1810645, "León":1579803}
lista_valores = [5**5, 12**2, 3050, 475*2]
print(min(ciudades_habitantes.keys()))
```

    León

```python
print(max(ciudades_habitantes.values()))
```

    1810645

```python
print(max(lista_valores))
```

    3125


## 4.9. - random

Python nos facilita un módulo (un conjunto de funciones disponibles para su uso) que nos permite generar selecciones pseudo-aleatorias* entre valores o secuencias.

Nombre del módulo:
```python
from random import *
```

* = Todos los métodos

También pueden importarse de manera independiente aquellos a utilizar.

**randint(min, max)**: devuelve un integer entre dos valores dados (ambos límites incluidos)

**uniform(min, max)**: devuelve un float entre un valor mínimo y uno máximo

**random(sin parámetros)**: devuelve un float entre 0 y 1

**choice(secuencia)**: devuelve un elemento al azar de una secuencia de valores (listas, tuples, rangos, etc.)

**shuffle(secuencia)**: toma una secuencia de valores mutable (como una lista), y la retorna cambiando el orden de sus elementos aleatoriamente.

* La mecánica en cómo se generan dichos valores aletorios viene en realidad predefinida en "semillas". Si bien sirve para todos los usos habituales, no debe emplearse con fines de seguridad o criptográficos, ya que son vulnerables.


## 4.10. - Comprensión de listas

La comprensión de listas es una manera dinámica de construir una lista. Ofrece una sintaxis más breve en la creación de una nueva lista basada en valores disponibles en otra secuencia. Vale la pena mencionar que la brevedad se logra a costo de una menor interpretabilidad. Sintaxis:
```python
	nueva_lista= [expresion for item in iterable if condicion == True]
```

*expresión* - 			fórmula matemática
*Item* - 				cada elemento del iterable
*iterable* - 			tuplas, sets, otras listas...
*condicion == True	* - 	operación lógica

Caso especial con else:
```python
	nueva_lista= [expresion if condicion == True else otra_expresion for item in iterable]
```

Ejemplo:
```python
	nueva_lista = [num**2 for num in range(10) if num < 5]
	print(nueva_lista)
```

    [0, 1, 4, 9, 16]

## 4.11. - match

En Python 3.10, se incorpora la coincidencia de patrones estructurales mediante las declaraciones match y case. Esto permite asociar acciones específicas basadas en las formas o patrones de tipos de datos complejos.
```python
match objeto:
  case <patron_1>:
    <accion_1>
  case <patron_2>:
    <accion_2>
  case <patron_3>:
    <accion_3>
  case _:
    <accion_comodin>
```

El caracter _ es un comodín que actúa como coincidencia si la misma no se produce en los casos anteriores.

Es posible detectar y deconstruir diferentes estructuras de datos: esto quiere decir que los patrones no son únicamente valores literales (strings o números), sino también estructuras de datos, sobre los cuales se buscan coindicencias de construcción.

## 4.12. - Proyecto del Día 4

La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un número y el programa puede responder cuatro cosas distintas:

- Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido un número que no está permitido.
- Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto. 
- Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la misma manera.  
- Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos intentos le ha tomado.

Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro número. Y así hasta que gane o hasta que se agoten los ocho intentos.

## Ficheros y documentación del día 4
- [01_operadores_comparacion.py](01_operadores_comparacion.py)
- [02_operadores_logicos.py](02_operadores_logicos.py)
- [03_control_de_frujo.py](03_control_de_frujo.py)
- [04_for.py](04_for.py)
- [05_while.py](05_while.py)
- [06_rango.py](06_rango.py)
- [07_enumerador.py](07_enumerador.py)
- [08_zip.py](08_zip.py)
- [09_min_max.py](09_min_max.py)
- [10_random.py](10_random.py)
- [11_comprension_listas.py](11_comprension_listas.py)
- [12_match.py](12_match.py)
- [13_programa04.py](13_programa04.py)

[Documentación del día](../doc_curso/04_adivinar_numero/)

---

Enlaces a todos los días: [dia 1 - creador de nombres](../dia_01/README.md) / [dia 2 - calculador de comisiones](../dia_02/README.md) / [dia 3 - analizador de texto](../dia_03/README.md) / [dia 4 - juego "adivina el número"](../dia_04/README.md) / [dia 5 - juego "El ahorcado"](../dia_05/README.md) / [dia 6 - recetario](../dia_06/README.md) / [dia 7 - cuenta bancaria](../dia_07/README.md) / [dia 8 - consola de turnos](../dia_08/README.md) / [dia 9 - buscador de números de serie](../dia_09/README.md) / [dia 10 - juego "Invasión espacial"](../dia_10/README.md) / [dia 11 - web scraping](../dia_11/README.md) / [dia 12 - gestor de restaurantes](../dia_12/README.md) / [dia 13 - asistente de voz](../dia_13/README.md) / [dia 14 - controlador de asistencia](../dia_14/README.md) / [dia 15 - machine learning](../dia_15/README.md) / [dia 16 - aplicación web de tareas pendientes](../dia_16/README.md)