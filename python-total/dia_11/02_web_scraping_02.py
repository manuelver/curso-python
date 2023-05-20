"""
Web scraping 
Descargar imágenes

"""
import bs4
import requests


resultado = requests.get(
    'https://www.escueladirecta.com/courses')


# Para poder extraer datos necesitamos
# un parser (analizador sintáctico)
# como beautiful soup
# Necesitaremos el texto y el tipo de motor de parsing
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Aislamos la url de la primera imagen
# que queremos descargar
imagen = sopa.select('.course-box-image')[0]['src']
print(imagen)

# Ahora cogemos el contenido del enlace
# (Tendrá un Response 200)
binario_imagen = requests.get(imagen)
# y mostramos el binario

# print(binario_imagen.content)

# Ahora preparamos un fichero para escribir
# wb significa "escribir binario"
# Abrimos el fichero, escribimos dentro y cerramos
f = open('mi_imagen.jpg', 'wb')
f.write(binario_imagen.content)
f.close()
