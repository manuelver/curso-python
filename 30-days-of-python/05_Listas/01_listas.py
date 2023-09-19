"""
01_listas.py
"""


# Ejercicios: Nivel 1

# 1. Declarar una lista vacía.
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos.
lista_mas_cinco = [1, 2, 3, 4, 5, 6, 7]

# 3. Encontrar la longitud de tu lista.
longitud_lista = len(lista_mas_cinco)

# 4. Obtener el primer elemento, el elemento del medio
# y el último elemento de la lista.
primer_elemento = lista_mas_cinco[0]
elemento_medio = lista_mas_cinco[longitud_lista // 2]
ultimo_elemento = lista_mas_cinco[-1]

# 5. Declarar una lista llamada `mixed_data_types`
# e inserta tu (nombre, edad, altura, estado civil, dirección).
mixed_data_types = ['Jorge', 30, 1.75, 'soltero', 'Calle 123']

# 6. Declarar una variable de lista llamada `it_companies`
# y asignar los valores iniciales Facebook, Google, Microsoft,
# Apple, IBM, Oracle y Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprime la lista usando `print()`.
print(it_companies)

# 8. Imprime el número de empresas en la lista.
print(len(it_companies))

# 9. Imprime la primera, la del medio y la última empresa.
print(
    f"""Primera empresa: {it_companies[0]}
Empresa del medio: {it_companies[len(it_companies) // 2]}
Última empresa: {it_companies[-1]}"""
)

# 10. Imprime la lista después de modificar una de las empresas.
it_companies[0] = 'Mecánica Hernandez'
print(it_companies)

# 11. Agrega una empresa de tecnología a `it_companies`.
it_companies.append('Floristería Rosita')

# 12. Inserta una empresa de tecnología en el medio de la lista de empresas.
it_companies.insert(len(it_companies) // 2, 'Cafetería Don Pepe')

# 13. Cambia uno de los nombres de `it_companies` a mayúsculas (¡excepto IBM!).
it_companies[3] = it_companies[3].upper()

# 14. Une las empresas de tecnología con una cadena '#;  '.
empresas_unidas = '#;  '.join(it_companies)

# 15. Comprueba si cierta empresa existe en la lista `it_companies`.
comprobar_empresa = 'IBM' in it_companies
print('IBM en la lista:', comprobar_empresa)

# 16. Ordena la lista usando el método `sort()`.
it_companies.sort()

# 17. Invierte la lista en orden descendente usando el método `reverse()`.
it_companies.sort(reverse=True)

# 18. Corta las primeras 3 empresas de la lista.
primeras_tres_empresas = it_companies[:3]

# 19. Corta las últimas 3 empresas de la lista.
ultimas_tres_empresas = it_companies[-3:]

# 20. Corta la empresa o empresas de tecnología del medio de la lista.
empresa_del_medio = it_companies[len(it_companies) // 2]

# 21. Elimina la primera empresa de tecnología de la lista.
it_companies.pop(0)

# 22. Elimina la empresa o empresas de tecnología del medio de la lista.
it_companies.remove(it_companies[len(it_companies) // 2])

# 23. Elimina la última empresa de tecnología de la lista.
it_companies.pop(-1)

# 24. Elimina todas las empresas de tecnología de la lista.
it_companies.clear()

# 25. Destruye la lista de empresas de tecnología.
del it_companies

# 26. Une las siguientes listas:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node', 'Express', 'MongoDB']
# Después de unir las listas en la pregunta 26, copia la lista unida
# y asígnala a una variable full_stack.
# Luego, inserta Python y SQL después de Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
full_stack = joined_list.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')
print(full_stack)

# Ejercicios: Nivel 2

# 1. La siguiente es una lista de edades de 10 estudiantes:
# edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Ordena la lista y encuentra la edad mínima y máxima.
edades.sort()
edad_min = edades[0]
edad_max = edades[-1]

# - Agrega nuevamente la edad mínima y máxima a la lista.
edades.append(edad_min)
edades.append(edad_max)

# - Encuentra la edad mediana (un solo elemento medio
# o dos elementos medios divididos por dos).
edad_mediana = edades[len(edades) // 2]
print(edad_mediana)
# - Encuentra la edad promedio (suma de todos los elementos divididos por su número).
edad_promedio = sum(edades) / len(edades)
print(edad_promedio)

# - Encuentra el rango de las edades (máximo menos mínimo).
rangos_edades = edad_max - edad_min

# - Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs().
abs_min_promedio = abs(edad_min - edad_promedio)
abs_max_promedio = abs(edad_max - edad_promedio)

# 2. Encuentra el país o países del medio en la lista de países.
# ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
# - Divide la lista de países en dos listas iguales si es par;
# si no, agrega un país más para la primera mitad.
paises = ['China', 'Rusia', 'EE. UU.',
          'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
if len(paises) % 2 == 0:
    primera_mitad = paises[:len(paises) // 2]
    segunda_mitad = paises[len(paises) // 2:]
else:
    primera_mitad = paises[:len(paises) // 2 + 1]
    segunda_mitad = paises[len(paises) // 2 + 1:]
print(primera_mitad, ',', segunda_mitad)

# - Desempaqueta los primeros tres países y el resto como países escandinavos.
primer_pais, segundo_pais, tercer_pais, *paises_escandinavos = paises
print(primer_pais, segundo_pais, tercer_pais, paises_escandinavos)
