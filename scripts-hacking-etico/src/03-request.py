"""
Instalar la biblioteca de Python `requests` 
y realizar una solicitud HTTP 
a la dirección URL `duckduckgo.com`
"""

import requests

# Realizar una solicitud GET a la URL
response = requests.get('https://duckduckgo.com/')

# Imprimir el código de estado y el contenido de la respuesta
print(f"Código de estado: \n{response.status_code}")
print('\n***\n')
print(f"Contenido de la respuesta: {response.text}")
