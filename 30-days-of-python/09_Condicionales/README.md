# Condicionales

Documento original en inglés: [Conditionals](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/09_Day_Conditionals/09_conditionals.md)

## Ejercicios

# Ejercicios: Nivel 1

1. Obtiene la entrada del usuario utilizando `input("Ingresa tu edad: ")`. Si el usuario tiene 18 años o más, muestra el mensaje: "Eres lo suficientemente mayor para conducir". Si es menor de 18 años, muestra el mensaje que indique cuántos años faltan para poder aprender a conducir. **Output:**

```
Ingresa tu edad: 30
Eres lo suficientemente mayor para aprender a conducir.
```

**Output:**

```
Ingresa tu edad: 15
Necesitas 3 años más para aprender a conducir.
```

2. Compara los valores de `mi_edad` y `tu_edad` usando `if... else`. ¿Quién es mayor (yo o tú)? Utiliza `input("Ingresa tu edad: ")` para obtener la edad como entrada. Puedes utilizar una condición anidada para imprimir "año" para una diferencia de edad de 1 año, "años" para diferencias mayores y un texto personalizado si `mi_edad` es igual a `tu_edad`. **Output:**

```
Ingresa tu edad: 30
Tu eres 5 años mayor que yo.
```

3. Obtiene dos números del usuario utilizando el prompt `input`. Si `a` es mayor que `b`, devuelve "a es mayor que b". Si `a` es menor que `b`, devuelve "a es menor que b". En caso contrario, devuelve "a es igual a b". **Output:**

```
Ingresa el número uno: 4
Ingresa el número dos: 3
4 es mayor que 3
```

## Ejercicios: Nivel 2

1. Escribe un código que asigne una calificación a los estudiantes según sus puntuaciones:
```
80-100: A
70-89: B
60-69: C
50-59: D
0-49: F
```

2. Comprueba si la estación es Otoño, Invierno, Primavera o Verano. Si la entrada del usuario es: Septiembre, Octubre o Noviembre, la estación es Otoño. Si la entrada es: Diciembre, Enero o Febrero, la estación es Invierno. Si la entrada es: Marzo, Abril o Mayo, la estación es Primavera. Si la entrada es: Junio, Julio o Agosto, la estación es Verano.

3. La siguiente lista contiene algunas frutas:
```
frutas = ['banana', 'naranja', 'mango', 'limón']
```

Si una fruta no existe en la lista, agrégala a la lista y muestra la lista modificada. Si la fruta ya existe, muestra el mensaje "Esa fruta ya existe en la lista".

## Ejercicios: Nivel 3

Aquí tenemos un diccionario llamado `persona`. ¡Siéntete libre de modificarlo!

```python
persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'país': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Calle Espacial',
        'código postal': '02210'
    }
}
```
- Comprueba si el diccionario persona tiene una clave llamada habilidades y, si es así, imprime la habilidad intermedia de la lista de habilidades.
- Comprueba si el diccionario persona tiene una clave llamada habilidades y, si es así, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.
- Si las habilidades de una persona son solo JavaScript y React, imprime "Es un desarrollador front-end". Si las habilidades incluyen Node, Python y MongoDB, imprime "Es un desarrollador back-end". Si las habilidades incluyen React, Node y MongoDB, imprime "Es un desarrollador fullstack". En caso contrario, imprime "título desconocido".
- Si la persona está casada y vive en Finlandia, imprime la información en el siguiente formato:
- 
```
Asabeneh Yetayeh vive en Finlandia. Está casado.
```
