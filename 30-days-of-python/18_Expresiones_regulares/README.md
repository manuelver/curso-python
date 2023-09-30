# Expresiones regulares

Documento original en inglés: [Regular Expressions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md)

## Ejercicios

### Ejercicios: Nivel 1

1. ¿Cuál es la palabra más frecuente en el siguiente párrafo?

```
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```
[
(6, 'love'),
(5, 'you'),
(3, 'can'),
(2, 'what'),
(2, 'teaching'),
(2, 'not'),
(2, 'else'),
(2, 'do'),
(2, 'I'),
(1, 'which'),
(1, 'to'),
(1, 'the'),
(1, 'something'),
(1, 'if'),
(1, 'give'),
(1, 'develop'),
(1, 'capabilities'),
(1, 'application'),
(1, 'an'),
(1, 'all'),
(1, 'Python'),
(1, 'If')
]
```

2. La posición de algunas partículas en el eje x horizontal son -12, -4, -3 y -1 en la dirección negativa, 0 en el origen, 4 y 8 en la dirección positiva. Extrae estos números de todo el texto y encuentra la distancia entre las dos partículas más lejanas.

```
puntos = ['-12', '-4', '-3', '-1', '0', '4', '8']
puntos_ordenados = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distancia = 8 - (-12)  # La distancia es 20
```


### Ejercicios: Nivel 2

1. Escribe un patrón que identifique si una cadena es una variable válida en Python.

```
es_variable_valida('primer_nombre')  # Verdadero
es_variable_valida('primer-nombre')  # Falso
es_variable_valida('1primer_nombre')  # Falso
es_variable_valida('nombre')         # Verdadero
```

### Ejercicios: Nivel 3

1. Limpia el siguiente texto. Después de limpiarlo, cuenta las tres palabras más frecuentes en la cadena.
```
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print(clean_text(sentence));
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
```
[Solución](01_regex.py)

[<< Day 17](../17_Manejo_de_excepciones/README.md) | [Day 19 >>](../19_Manipulación_de_archivos/README.md)
