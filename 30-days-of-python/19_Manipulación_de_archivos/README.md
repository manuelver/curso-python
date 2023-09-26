# Manipulación de archivos

Documento original en inglés: [file handling](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/19_Day_File_handling/19_file_handling.md)

## Ejercicios

### Ejercicios: Nivel 1

1. Escribe una función que cuente el número de líneas y palabras en un texto. Todos los archivos se encuentran en la carpeta data:
a) Lee el archivo obama_speech.txt y cuenta el número de líneas y palabras
b) Lee el archivo michelle_obama_speech.txt y cuenta el número de líneas y palabras
c) Lee el archivo donald_speech.txt y cuenta el número de líneas y palabras
d) Lee el archivo melina_trump_speech.txt y cuenta el número de líneas y palabras


2. Lee el archivo de datos countries_data.json en el directorio data, crea una función que encuentre los diez idiomas más hablados.

```py
# Tu resultado debería lucir de la siguiente manera
print(idiomas_mas_hablados(archivo='./data/countries_data.json', top=10))
[
{'idioma': 'Inglés', 'cantidad': 91},
{'idioma': 'Francés', 'cantidad': 45},
{'idioma': 'Árabe', 'cantidad': 25},
{'idioma': 'Español', 'cantidad': 24},
{'idioma': 'Ruso', 'cantidad': 9},
{'idioma': 'Portugués', 'cantidad': 9},
{'idioma': 'Holandés', 'cantidad': 8},
{'idioma': 'Alemán', 'cantidad': 7},
{'idioma': 'Chino', 'cantidad': 5},
{'idioma': 'Suajili', 'cantidad': 4}
]

# Tu resultado debería lucir de la siguiente manera
print(idiomas_mas_hablados(archivo='./data/countries_data.json', top=3))
[
{'idioma': 'Inglés', 'cantidad': 91},
{'idioma': 'Francés', 'cantidad': 45},
{'idioma': 'Árabe', 'cantidad': 25}
]
```

3. Lee el archivo de datos countries_data.json en el directorio data, crea una función que genere una lista de los diez países más poblados.

```py
# Tu resultado debería lucir de la siguiente manera
print(paises_mas_poblados(archivo='./data/countries_data.json', top=10))
[
{'país': 'China', 'población': 1377422166},
{'país': 'India', 'población': 1295210000},
{'país': 'Estados Unidos de América', 'población': 323947000},
{'país': 'Indonesia', 'población': 258705000},
{'país': 'Brasil', 'población': 206135893},
{'país': 'Pakistán', 'población': 194125062},
{'país': 'Nigeria', 'población': 186988000},
{'país': 'Bangladesh', 'población': 161006790},
{'país': 'Federación Rusa', 'población': 146599183},
{'país': 'Japón', 'población': 126960000}
]

# Tu resultado debería lucir de la siguiente manera
print(paises_mas_poblados(archivo='./data/countries_data.json', top=3))
[
{'país': 'China', 'población': 1377422166},
{'país': 'India', 'población': 1295210000},
{'país': 'Estados Unidos de América', 'población': 323947000}
]
```

### Ejercicios: Nivel 2

1. Extrae todas las direcciones de correo electrónico entrantes como una lista del archivo email_exchange_big.txt.
2. Encuentra las palabras más comunes en el idioma inglés. Llama a tu función encontrar_palabras_mas_comunes, tomará dos parámetros: una cadena o un archivo y un número entero positivo que indicará la cantidad de palabras. Tu función devolverá una lista de tuplas en orden descendente. Comprueba el resultado.

```py
# Tu resultado debería lucir de la siguiente manera
print(encontrar_palabras_mas_comunes('muestra.txt', 10))
[(10, 'the'),
(8, 'be'),
(6, 'to'),
(6, 'of'),
(5, 'and'),
(4, 'a'),
(4, 'in'),
(3, 'that'),
(2, 'have'),
(2, 'I')]

# Tu resultado debería lucir de la siguiente manera
print(encontrar_palabras_mas_comunes('muestra.txt', 5))
[(10, 'the'),
(8, 'be'),
(6, 'to'),
(6, 'of'),
(5, 'and')]
```

3. Utiliza la función encontrar_palabras_mas_comunes para encontrar:
a) Las diez palabras más frecuentes utilizadas en el discurso de Obama
b) Las diez palabras más frecuentes utilizadas en el discurso de Michelle
d) Las diez palabras más frecuentes utilizadas en el discurso de Melina
c) Las diez palabras más frecuentes utilizadas en el discurso de Trump

4. Escribe una aplicación Python que verifique la similitud entre dos textos. Toma un archivo o una cadena como parámetro y evaluará la similitud entre los dos textos. Es posible que necesites un par de funciones: una para limpiar el texto (limpiar_texto), una para eliminar las palabras de soporte (eliminar_palabras_soporte) y finalmente para verificar la similitud (verificar_similitud_texto). La lista de palabras de paro se encuentra en el directorio data.

5. Encuentra las 10 palabras más repetidas en romeo_and_juliet.txt.

6. Lee el archivo CSV de hacker news y averigua:
a) Cuántas líneas contienen python o Python
b) Cuántas líneas contienen JavaScript, javascript o Javascript
c) Cuántas líneas contienen Java y no JavaScript

[<< Day 18](../18_Expresiones_regulares/README.md) | [Day 20 >>](../20_Gestor_de_paquetes_de_Python/README.md)
