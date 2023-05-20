"""
Web scraping básico

Con las librerias beautifulsoup4, lxml y requests

"""
import bs4
import requests

resultado = requests.get(
    'https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

# el tipo nos muestra que es de tipo Response
print(type(resultado))
print()


# Si intentamos imprimir el texto nos mostrará todo el contenido html, css ...
# print(resultado.text)

# Para poder extraer datos necesitamos un parser (analizador sintáctico)
# como beautiful soup
# Necesitaremos el texto y el tipo de motor de parsing

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


# Con lo cual, ahora en la variable ya no es un string
# y este modo de texto de tipo bs4
# permite navegar mejor por él
print(type(sopa))
print()


# Podemos escoger las etiquetas, por ejemplo title
print(sopa.select('title'))
print()


# Nos dará una lista, porque puede haber más de un elemento
# que podemos contar con len
print(f"Tiene {len(sopa.select('p'))} párrafos.")
print()


# Podemos seleccionar de la lista el índice del elemento
# que queremos y además pedir que nos devuelva tan solo
# el texto de dentro del elemento
print(sopa.select('p')[1].getText())
print()


# Vamos a buscar un párrafo en concreto
parrafo_especial = sopa.select('p')[3].getText()
print(parrafo_especial)
print()


# Ahora vamos a coger elementos de la columna lateral
# Todos los títulos
titulos_columna_lateral = sopa.select('.sidebar-container article .post-title')
for title in titulos_columna_lateral:
    print(title.getText())
    print()

# Mostrar un párrafo concreto
parrafos_columna_lateral = sopa.select(
    '.sidebar-container article .snippet-item')
print(parrafos_columna_lateral[0].getText())
