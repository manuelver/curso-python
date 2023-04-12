"""
Web scraping básico

Con las librerias beautifulsoup4, lxml y requests

"""

import bs4
import requests

raiz = 'http://books.toscrape.com/catalogue/page-'
extension = '.html'


def comprobar_enlaces(http, ext):
    """ Comprobar si el enlace existe """

    # Variables
    enlaces = []
    fin_url = True
    page = 0

    # Bucle para formar url y añadir a una lista
    while fin_url:

        page += 1
        page = str(page)

        enlace = http + page + ext

        resultado = requests.get(enlace)

        if resultado:
            enlaces.append(enlace)
            page = int(page)
            # BORRAR CUANDO ESTE LISTO EL RESTO DEL DOCUMENTO
            break
        else:
            fin_url = False

    return enlaces


print(comprobar_enlaces(raiz, extension))


# sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
