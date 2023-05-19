
# Día 2 - Programa un calculador de comisiones

## Índice
- [Día 2 - Programa un calculador de comisiones](#día-2---programa-un-calculador-de-comisiones)
  - [Índice](#índice)
  - [2.1. - Tipos de datos](#21---tipos-de-datos)
  - [2.2. - Variables](#22---variables)
    - [2.2.1 - Ejemplo de uso de variables](#221---ejemplo-de-uso-de-variables)
  - [2.3. - Nombres de variables](#23---nombres-de-variables)
    - [2.3.1. - Reglas](#231---reglas)
  - [2.4. - integers \& floats](#24---integers--floats)
    - [2.4.1. - int](#241---int)
    - [2.4.2. - float](#242---float)
  - [2.5. - Conversiones](#25---conversiones)
  - [2.6. - Formatear cadenas](#26---formatear-cadenas)
  - [2.7. - Operadores matemáticos](#27---operadores-matemáticos)
  - [2.8. - Redondeo](#28---redondeo)
    - [2.8.1. - algunos ejemplos de uso](#281---algunos-ejemplos-de-uso)
  - [2.9. - Proyecto del Día 2](#29---proyecto-del-día-2)
  - [Ficheros y documentación del día 2](#ficheros-y-documentación-del-día-2)

## 2.1. - Tipos de datos
En Python tenemos varios tipos o estructuras de datos, que son fundamentales en programación ya que almacenan información, y nos permiten manipularla. 

| texto (srt) | números (int, float) | booleanos (bool) |
| ----------- | -------------------- | ---------------- |
| "Python"    | Int 3                | True             |
| "750"       | float 3.0            | False            |


| estructuras     | Descripción        | mutable            | ordenada (Tiene índice) | duplicados                  |
| --------------- | ------------------ | ------------------ | ----------------------- | --------------------------- |
| listas []       | *list*             | :heavy_check_mark: | :heavy_check_mark:      | :heavy_check_mark:          |
| tuplas ()       | *Entre paréntesis* | :x:                | :heavy_check_mark:      | :heavy_check_mark:          |
| sets {}         | *Entre llaves*     | :heavy_check_mark: | :x:                     | :x:                         |
| diccionarios {} | *dic key:valor*    | :heavy_check_mark: | :x: *                   | :x: : :heavy_check_mark: ** |

*: En Python 3.7+, existen consideraciones		**: key es única; value puede repetirse


## 2.2. - Variables

Las variables son espacios de memoria que almacenan valores o datos de distintos tipos, y (como su nombre indica) pueden variar. Se crean en el momento que se les asigna un valor, por lo cual en Python no requerimos declararlas previamente.

### 2.2.1 - Ejemplo de uso de variables

```python
pais = "México"
nombre = input("Escribe tu nombre: ")
print("Tu nombre es " + nombre)
num1 = 55
num2 = 45
print(nun1 + num2)
```

    100

## 2.3. - Nombres de variables

Existen convenciones y buenas prácticas asociadas al nombre de las variables creadas en Python. Las mismas tienen la intención de facilitar la interpretabilidad y mantenimiento del código creado.

### 2.3.1. - Reglas

1. **Legible**: nombre de la variable es relevante según su contenido
2. **Unidad**: no existen espacios (La práctica en Python es incorporar guiones bajos *ejemplo_variable*)
3. **Hispanismos**: omitir signos específicos del idioma español, como tildes o la letra ñ
4. **Números**: los nombres de las variables no deben empezar por números (aunque pueden contenerlos al final)
5. **Signos/símbolos**: no se deben incluir : `" ' , < > / ? | \ ( ) ! @ # $%^&*~-+`
6. **Palabras clave**: no utilizamos palabras reservadas por Python.

## 2.4. - integers & floats

Existen dos tipos de datos numéricos básicos en Python: int y float. Como toda variable en Python, su tipo queda definido al asignarle un valor a una variable. La función type() nos permite obtener el tipo de valor almacenado en una variable.

### 2.4.1. - int
Int, o integer, es un número entero, positivo o negativo, sin decimales, de un largo indeterminado.

```python
Num1 = 7
print(type(num1))
```

    <class 'int'>

### 2.4.2. - float

Float, o "número de punto flotante" es un número que puede ser positivo o negativo, que a su vez contiene una o más posiciones decimales.
```python
Num2 = 7.525587
print(type(num2))
```

    <class 'float'>

## 2.5. - Conversiones
Python realiza conversiones implícitas de tipos de datos automáticamente para operar con valores numéricos. En otros casos, necesitaremos generar una conversión de manera explícita.

```python
int(var)
```

    <class 'int'>			"""Convierte el dato en integer"""

```python
float(var)
```

    <class 'float'>			"""Convierte el dato en float"""

## 2.6. - Formatear cadenas

Para facilitar la concatenación de variables y texto en Python, contamos con dos herramientas que nos evitan manipular las variables, para incorporarlas directamente al texto:
- Función format: se encierra las posiciones de las variables entre corchetes { }, y a continuación del string llamamos a las variables con la función format
```python
print("Mi auto es {} y de matrícula {}".format(color_auto,matricula))
```

- Cadenas literales (f-strings): a partir de Python 3.8, podemos anticipar la concatenación de variables anteponiendo f al string
```python
print(f"Mi auto es {color_auto} y de matrícula {matricula}")
```

## 2.7. - Operadores matemáticos

Veamos cuáles son los operadores matemáticos básicos de Python, que utilizaremos para realizar cálculos:

| Descripción                                       | Operador |
| ------------------------------------------------- | -------- |
| Suma                                              | +        |
| Resta                                             | -        |
| Multiplicación                                    | *        |
| División                                          | /        |
| Cociente (división "al piso". Redondeo)           | //       |
| Resto (módulo) (Útil para detectar valores pares) | %        |
| Potencia                                          | **       |
| Raíz cuadrada	(¡es un caso especial de potencia!) | **0.5    |

## 2.8. - Redondeo

El redondeo facilita la interpretación de los valores calculados al limitar la cantidad de decimales que se muestran en pantalla. También, nos permite aproximar valores decimales al entero más próximo.

round(number,ndigits)
- *number* - valor a redondear cantidad de
- *ndigits* - Cantidad de decimales (si se omite, el resultado es entero)

### 2.8.1. - algunos ejemplos de uso

```python
print(round(100/3))
```

    33

```python
print(round(12/7,2))
```

    1.71

## 2.9. - Proyecto del Día 2

La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le corresponde por las comisiones.

Esto no es un programa complejo, pero es entendible que pueda complicarse cuando estás aprendiendo. Por más que lo que has aprendido hasta ahora es muy simple, ponerlo todo junto en un solo programa puede ser complejo, por lo que te doy un par de ayudas: 
- Este programa debería comenzar preguntando cosas al usuario, por lo tanto, vas a necesitar input para poder recibir los ingresos del usuario y deberías usar variables para almacenar esos ingresos. Recuerda que los ingresos de usuarios se almacenan como strings. Por lo tanto, deberías convertir uno de esos ingresos en un float para poder hacer operaciones con él. 
- ¿Y qué operaciones necesitas hacer? Bueno, calcular el 13% del número que haya ingresado el usuario. Es decir, que debes multiplicar ese número por 13 y luego dividirlo por 100. Recuerda almacenar ese resultado en una variable.
- Sería bueno que para imprimir en pantalla el resultado te asegures de que esa información no tenga más de dos decimales, para que sea fácil de leer, y luego organiza todo eso en un string al que debes dar formato. Recuerda que conocimos dos maneras de hacerlo y cualquiera de ellas es válida. 

## Ficheros y documentación del día 2
- [01_variables.py](01_variables.py)
- [02_intengers_floats.py](02_intengers_Floats.py)
- [02_intengers_math.py](02_intengers_math.py)
- [03_Conversiones.py](03_Conversiones.py)
- [04_format.py](04_format.py)
- [05_operadores.py](05_operadores.py)
- [06_programa02.py](06_programa02.py)

[Documentación curso](../doc_curso/02_calculador_comisiones/)
