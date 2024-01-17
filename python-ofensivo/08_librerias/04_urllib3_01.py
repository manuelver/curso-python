#!/usr/bin/env python3
"""
urllin3 es la base de requests, a más bajo nivel es más compleja de usar.

# https://httpbin.org/get

Para enviar a POST:
- Datos en bruto: body='...'
- Datos en form: fields={'key': 'value'}
- Datos en JSON: body=json.dumps({'key': 'value'})

"""

import urllib3
import json

http = urllib3.PoolManager() # Controlador de conexiones

data = "Esto es una prueba"
encoded_data = data.encode() # Convertir a bytes

dict_data = {'foo': 'bar'}
encoded_dict_data = json.dumps(dict_data).encode()

r = http.request(
    'POST', 
    'https://httpbin.org/post', 
    # body=encoded_data
    body=encoded_dict_data,
    headers={'Content-Type': 'application/json'}
)

print(r.data.decode())


