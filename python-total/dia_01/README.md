# Día 1 - Programa un creador de nombres

## Índice

- [Día 1 - Programa un creador de nombres](#día-1---programa-un-creador-de-nombres)
  - [Índice](#índice)
  - [1.1. - print](#11---print)
    - [1.1.1. - Mostrar texto](#111---mostrar-texto)
    - [1.1.2. - Mostrar números](#112---mostrar-números)
  - [1.2. - strings](#12---strings)
    - [1.2.1. - Concatenación](#121---concatenación)
    - [1.2.2. - Caracteres especiales](#122---caracteres-especiales)
  - [1.3. - input](#13---input)
  - [1.4. - Proyecto del Día 1](#14---proyecto-del-día-1)
  - [Ficheros y documentación del día 1](#ficheros-y-documentación-del-día-1)

## 1.1. - print
print - Declaración que al ejecutarse muestra (o imprime) en pantalla el argumento que se introduce dentro de los paréntesis.

### 1.1.1. - Mostrar texto

Ingresamos entre comillas simples o dobles los caracteres de texto que deben mostrarse en pantalla.

```python
print("Hola mundo")
```

Output

    Hola mundo

### 1.1.2. - Mostrar números

Podemos entregarle a print() el número que debe mostrar, o una operación matemática a resolver. No empleamos comillas en estos casos.

```python
print(150 + 50)
```

output

    200

## 1.2. - strings

Los strings en Python son un tipo de dato formado por cadenas (o secuencias) de caracteres de cualquier tipo, formando un texto.

### 1.2.1. - Concatenación

Unificación de cadenas de texto:
```python
print("Hola" + " " + "mundo")
```
output

    Hola mundo

### 1.2.2. - Caracteres especiales

Indicamos a la consola que el caracter a continuación del símbolo \ debe ser tratado como un caracter especial.

- `\"` 	--> Imprime comillas
- `\n` 	--> Separa texto en una nueva linea
- `\t` 	--> Imprime un tabulador
- `\\` 	--> Imprime la barra invertida textualmente

## 1.3. - input

Función que permite al usuario introducir información por medio del teclado al ejecutarse, otorgándole una instrucción acerca del ingreso solicitado. El código continuará ejecutándose luego de que el usuario realice la acción.

```python
input("Dime tu nombre: ")
```
output

    Dime tu nombre: |

```python
print("Tu nombre es " + input("Dime tu nombre: "))
```

output

    Dime tu nombre: Federico
    Tu nombre es Federico

## 1.4. - Proyecto del Día 1
Imagina esta situación: tu mejor amigo ha puesto una fábrica de cerveza y tiene todo listo. Su producto es fantástico, tiene cuerpo, buen sabor, buen color, el nivel justo de espuma… pero le falta una identidad. No se le ocurre qué nombre ponerle su cerveza para que tenga una identidad única y original. Entonces vienes tú y le dices "No te preocupes, yo voy a crear un programa que te va a hacer dos preguntas y luego te va a decir cuál es el nombre de tu cerveza". Así de simple. 

Ya sé que en el mundo real no necesitaríamos desarrollar un software solo para hacer dos preguntas, pero hasta que aprendamos más funcionalidades los programas van a tener que mantenerse en el terreno de lo simple. Igualmente, si está recién comenzando, este va a ser todo un desafío.

Vas a crear un código en Python que le pida a tu amigo que responda dos preguntas que requieran una sola palabra cada una y que luego le muestre en pantalla esas palabras combinadas, para formar una marca creativa.

Puedes usar las preguntas que quieras. La idea es que el resultado sea original, creativo, y hasta cómico, y si quieres agregar dificultad al desafío, te sugiero que intentes que el nombre de la cerveza se imprima entre comillas. Recuerda que hay diferentes formas de que la función print muestre las comillas sin cortar el string, y que ingrese la impresión final en al menos dos líneas utilizando saltos de línea dentro del código.

Intenta hacerlo por tu cuenta y si se complica, no te preocupes, en la próxima elección lo vamos a resolver juntos.

## Ficheros y documentación del día 1
- [main.py](main.py)
- [primer_programa.py](primer_programa.py)
- [programa01.py](programa01.py)

[Documentación del día](../doc_curso/01_creador_de_nombres/)

---

Enlaces a todos los días: [dia 1 - creador de nombres](../dia_01/README.md) / [dia 2 - calculador de comisiones](../dia_02/README.md) / [dia 3 - analizador de texto](../dia_03/README.md) / [dia 4 - juego "adivina el número"](../dia_04/README.md) / [dia 5 - juego "El ahorcado"](../dia_05/README.md) / [dia 6 - recetario](../dia_06/README.md) / [dia 7 - cuenta bancaria](../dia_07/README.md) / [dia 8 - consola de turnos](../dia_08/README.md) / [dia 9 - buscador de números de serie](../dia_09/README.md) / [dia 10 - juego "Invasión espacial"](../dia_10/README.md) / [dia 11 - web scraping](../dia_11/README.md) / [dia 12 - gestor de restaurantes](../dia_12/README.md) / [dia 13 - asistente de voz](../dia_13/README.md) / [dia 14 - controlador de asistencia](../dia_14/README.md) / [dia 15 - machine learning](../dia_15/README.md) / [dia 16 - aplicación web de tareas pendientes](../dia_16/README.md)
