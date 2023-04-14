"""
Web scraping 
nivel intermedio

Con las librerias beautifulsoup4, lxml y requests

"""

import bs4
import requests

# Variables
URL_BASE = 'http://books.toscrape.com/catalogue/page-{}.html'
FIN_URL = True
PAGE = 0
lista_titulos = []

print(f'\nLIBROS CON 4 O 5 ESTRELLAS\n')

# Bucle para formar url y añadir a una lista
while FIN_URL:

    PAGE += 1
    ENLACE = URL_BASE.format(PAGE)

    resultado = requests.get(ENLACE)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Si existe la url
    if resultado:

        # Todos los títulos
        libros = sopa.select('.product_pod')
        # Mostramos la página y el enlace
        print(f'\nNÚMERO DE PÁGINA: {PAGE}\nENLACE: {ENLACE}\nLIBROS:')

        # Seleccionamos uno a uno cada libro
        for libro in libros:

            # Seleccionamos los libros que tengan 4 o 5 estrellas
            if libro.select('.star-rating.Four') or libro.select('.star-rating.Five'):

                # Seleccionamos el texto del title del elemento
                titulo_libro = libro.select('a')[1]['title']

                # Mostramos el libro
                print(f'\t- \"{titulo_libro}\"')
    # Si no existe la url
    else:
        print("")
        FIN_URL = False
