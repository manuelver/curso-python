"""
Módulo re

Expresiones regulares

Operadores especiales:
	[ ]		un set de caracteres
	.		un carácter cualquiera
	^		inicia con
	$		finaliza con
	|		operador lógico "O"

Cuantificadores: 
	*		cero o más ocurrencias: 0 - n
	+		una o más ocurrencias: 1 - n
	?		cero o una ocurrencia: 0 - 1
	{ }		un número especificado de ocurrencias
    {n}     se repite n veces
    {n,m}     se repite de n a m veces
    {n, }     se repite de n veces hacia arriba

Carácteres especiales:
	\d		dígito numérico
	\D		NO numérico
	\w		caracter alfanumérico
	\W		NO alfanumérico
	\s		espacio en blanco
	\S		NO espacio en blanco

"""

import re

# Buscar este patrón: ### - #### - ####
# De diferentes formas:
patron1 = r'\d\d\d-\d\d\d-\d\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{4}'
# Si no existe dirá: Node
verificacion01 = re.search(patron1, '234-233-l23l')
# Si existe dirá que tiene match:
# <re.Match object; span=(0, 12), match='234-233-1231'>
verificacion02 = re.search(patron1, '234-233-1231')
print(
    f'La verificación 1 es {verificacion01}\nLa verificación 2 es {verificacion02}')


print()

# Usando un texto

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

palabra = 'ayuda' in texto

print(f'Es {palabra} que la palabra ayuda está en el texto')
# Con expresión regular
patron03 = 'ayuda'

# Busqueda es un objeto regular expresión
# en concreto search
busqueda01 = re.search(patron03, texto)
# con lo cual, tiene módulos
# span indica la ubicación
print(busqueda01.span())
# start indica la ubicación del inicio
print(busqueda01.start())
# end indica la ubicación del final
print(busqueda01.end())


print()
# Objeto findall
# Mete en una lista cada vez que aparece el patron
busqueda02 = re.findall(patron03, texto)
print(busqueda02)
# Podemos ver el número de veces con len
print(len(busqueda02))


print()
# Podemos iterar la búsqueda
# con el módulo finiter para
# tener información de cada resultado encontrado
for hallazgo in re.finditer(patron03, texto):
    print(hallazgo.span())


print()
# Vamos a buscar el número de teléfono del texto
# se puede escapar los paréntesis para que los búsque
# y agrupar con parétesis
patron04 = r'\((\d{3})\)-(\d{3})-(\d{4})'

busqueda03 = re.search(patron04, texto)
# Podemos mostrar el resultado mostrando los grupos
print(busqueda03.group())
# y como además los hemos encerrado en paréntesis
# podemos llamar a cada uno de los grupos
print(busqueda03.group(2))

# Podemos controlar la entrada del usuario
# ⚠️ Cuidao: Este método no sirve para verificar contraseñas
# por ejemplo:
#
print(""" 
Introduce una clave con las condiciones:
- Empezar con una letra
- En total 8 carácteres
""")

clave = input('> ')
patron05 = r'\D{1}\w{7}'
chequear = re.search(patron05, clave)
print(chequear)


print()
# Operadores especiales
# or
buscarunouotro = re.search(r'online|offline', texto)
print(buscarunouotro.group())


print()
# Comodin en un espacio con punto
comodin01 = re.search(r'...vicio', texto)
print(comodin01.group())


print()
# Comodin inicio con ^
# Por ejemplo, que el primer caracter no sea un dígito
comodin02 = re.search(r'^\D', texto)
print(comodin02.group())


print()
# Comodin final con $
# Por ejemplo, que el último caracter sea un dígito
comodin03 = re.search(r'\d$', texto)
print(comodin03)


print()
# Comodin de un set de caracteres con [^]
# Por ejemplo, todos los que incluyan un carácter vacío
comodin04 = re.findall(r'[^\S]', texto)
print(f'El texto contiene {len(comodin04)} espacios en blanco')


print()
# Comodin de un set de caracteres con [^+]
# Ahora, además, va a agrupar los que no son
# espacios vacíos en strings dentro de la lista
# Seleciona cada inicio con caracter hasta que
# encuentra otro espacio en blanco.
comodin05 = re.findall(r'[^\s]+', texto)
print(comodin05)

# Con esto y join podemos unir de nuevo el texto pero
# sustituyendo con guiones, por ejemplo.
# Puede servir para corregir nombres de ficheros o directorios.
print('-'.join(comodin05))


# EJERCICIOS


print()
# Verificar si es un mail


def verificar_email(email):
    """ Verificar sin es un mail .com """
    patron = r'[\w]*@[\w]*\.com[\w]*'
    verificacion = re.search(patron, email)

    if verificacion:
        print("Ok. Es un mail")
    else:
        print("La dirección de email es incorrecta")


verificar_email("email@mail.com")

print()
# Verificar saludo


def verificar_saludo(frase):
    """ Verificar si saluda con Hola """
    patron = r'^Hola'
    verificacion = re.search(patron, frase)

    if verificacion:
        print("Ok. Este mensaje tiene saludo al inicio")
    else:
        print("No has saludado")


verificar_saludo("Hola, que tal?")


print()
# Verificar Código postal.
# Dos caracteres alfanuméricos
# y cuatro numéricos a continuación
# (ejemplo: XX1234)


def verificar_cp(cp):
    """ Verificar si saluda con Hola """
    patron = r'^\w{2}\d{4}$'
    verificacion = re.search(patron, cp)

    if verificacion:
        print("Ok. Es un código postal")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp("XX1234")
