"""
01_condicionales.py
"""

# Ejercicios: Nivel 1

# 1. Obtiene la entrada del usuario utilizando `input("Ingresa tu edad: ")`.
# Si el usuario tiene 18 años o más, muestra el mensaje: "Eres lo suficientemente mayor para conducir".
# Si es menor de 18 años, muestra el mensaje que indique cuántos años faltan para poder aprender a conducir.
edad = int(input("Ingresa tu edad: "))
if edad > 65:
    print("Quizá en la jubilación no es el mejor momento para aprender a conducir.")
elif edad < 18:
    print(f"Necesitas {18 - edad} años más para aprender a conducir.")
else:
    print("Eres lo suficientemente mayor para aprender a conducir.")

# 2. Compara los valores de `mi_edad` y `tu_edad` usando `if... else`.
# ¿Quién es mayor (yo o tú)?
# Utiliza `input("Ingresa tu edad: ")` para obtener la edad como entrada.
# Puedes utilizar una condición anidada para imprimir "año" para una diferencia de edad de 1 año,
# "años" para diferencias mayores y un texto personalizado si `mi_edad` es igual a `tu_edad`.
mi_edad = 32
tu_edad = int(input("Ingresa tu edad: "))
diferencia = mi_edad - tu_edad
if mi_edad > tu_edad:
    if diferencia == 1:
        print(f"Yo soy {diferencia} año mayor que tú.")
    else:
        print(f"Yo soy {diferencia} años mayor que tú.")
elif mi_edad < tu_edad:
    if diferencia == 1:
        print(f"Tú eres {diferencia} año mayor que yo.")
    else:
        print(f"Tú eres {diferencia} años mayor que yo.")
else:
    print("Tenemos la misma edad.")

# 3. Obtiene dos números del usuario utilizando el prompt `input`.
# Si `a` es mayor que `b`, devuelve "a es mayor que b".
# Si `a` es menor que `b`, devuelve "a es menor que b".
# En caso contrario, devuelve "a es igual a b".
a = int(input("Ingresa el número a: "))
b = int(input("Ingresa el número b: "))
if a > b:
    print(f"El número a ({a}) es mayor que el número b ({b})")
elif a < b:
    print(f"El número a ({a}) es menor que el número b ({b})")
else:
    print(f"El número a ({a}) es igual al número b ({b})")

# Ejercicios: Nivel 2

# 1. Escribe un código que asigne una calificación
# a los estudiantes según sus puntuaciones:
# 80-100: A
# 70-89: B
# 60-69: C
# 50-59: D
# 0-49: F
puntuacion = int(
    input("Ingresa la puntuación del estudiante (Entre 0 y 100): "))
if puntuacion >= 80:
    print("A")
elif puntuacion >= 70:
    print("B")
elif puntuacion >= 60:
    print("C")
elif puntuacion >= 50:
    print("D")
else:
    print("F")

# 2. Comprueba si la estación es Otoño, Invierno, Primavera o Verano.
# Si la entrada del usuario es: Septiembre, Octubre o Noviembre, la estación es Otoño.
# Si la entrada es: Diciembre, Enero o Febrero, la estación es Invierno.
# Si la entrada es: Marzo, Abril o Mayo, la estación es Primavera.
# Si la entrada es: Junio, Julio o Agosto, la estación es Verano.
mes = input("Ingresa el mes: ")
if mes in ['Diciembre', 'Enero', 'Febrero']:
    print("Invierno")
elif mes in ['Marzo', 'Abril', 'Mayo']:
    print("Primavera")
elif mes in ['Junio', 'Julio', 'Agosto']:
    print("Verano")
else:
    print("Otoño")

# 3. La siguiente lista contiene algunas frutas:
# frutas = ['banana', 'naranja', 'mango', 'limón']
# Si una fruta no existe en la lista, agrégala y muestra la lista modificada.
# Si la fruta ya existe, muestra el mensaje "Esa fruta ya existe en la lista".
frutas = ['banana', 'naranja', 'mango', 'limón']
fruta = input("Ingresa una fruta: ")
if fruta in frutas:
    print("Esa fruta ya existe en la lista.")
else:
    frutas.append(fruta)
    print('\n'.join(frutas))

# Ejercicios: Nivel 3

# Aquí tenemos un diccionario llamado `persona`.
# ¡Siéntete libre de modificarlo!
persona = {
    'nombre': 'Armando',
    'apellido': 'Guerra',
    'edad': 32,
    'país': 'Guatemala',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Calle Espacial',
        'código postal': '02210'
    }
}

# Comprueba si el diccionario persona tiene una clave llamada habilidades,
# si es así, imprime la habilidad intermedia de la lista de habilidades.
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    habilidades_length = len(habilidades)
    if habilidades_length % 2 == 0:
        index = habilidades_length // 2 - 1
        habilidad_intermedia = habilidades[index:index+2]
    else:
        index = habilidades_length // 2
        habilidad_intermedia = habilidades[index]
    print(f"Habilidad intermedia: {habilidad_intermedia}")

# Comprueba si el diccionario persona tiene una clave llamada habilidades,
# si es así, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    if 'Python' in habilidades:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona no tiene la habilidad 'Python'.")

# Si las habilidades de una persona son solo JavaScript y React,
# imprime "Es un desarrollador front-end".
# Si las habilidades incluyen Node, Python y MongoDB,
# imprime "Es un desarrollador back-end".
# Si las habilidades incluyen React, Node y MongoDB,
# imprime "Es un desarrollador fullstack".
# En caso contrario, imprime "título desconocido".
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    if habilidades == ['JavaScript', 'React']:
        print("Es un desarrollador front-end.")
    elif set(habilidades) == set(['Node', 'Python', 'MongoDB']):
        print("Es un desarrollador back-end.")
    elif set(habilidades) == set(['React', 'Node', 'MongoDB']):
        print("Es un desarrollador fullstack.")
    else:
        print("Título desconocido.")

# Si la persona está casada y vive en Guatemala,
# imprime la información en el siguiente formato:
# Asabeneh Yetayeh vive en Guatemala. Está casado.
if 'casado' in persona and 'país' in persona:
    if persona['casado'] and persona['país'] == 'Guatemala':
        nombre_completo = persona['nombre'] + ' ' + persona['apellido']
        print(f"{nombre_completo} vive en Guatemala. Está casado.")
