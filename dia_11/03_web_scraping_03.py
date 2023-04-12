"""
Web scraping básico

Con las librerias beautifulsoup4, lxml y requests

"""

import bs4
import requests

# Variables
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'
fin_url = True
page = 0
lista_titulos = []

# Bucle para formar url y añadir a una lista
while fin_url:

    page += 1
    page = str(page)

    enlace = url_base.format(page)

    resultado = requests.get(enlace)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    if resultado:
        page = int(page)

        # Todos los títulos
        titulos = sopa.select('.product_pod a')

        for title in titulos:
            if title.get('title') != None:
                lista_titulos.append(title.get('title'))

    else:
        fin_url = False

print(lista_titulos)
