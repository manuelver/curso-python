#!/usr/bin/env python3

import requests

url = 'http://github.com'

# r = requests.get(url, allow_redirects=False  # Para que no haga reenvíos)
r = requests.get(url)

# print(r.url)

for request in r.history:
    print(f"\n[+] Hemos pasado por el dominio {request.url} con un código de estado {request.status_code}")

print(f"\n[+] URL final: {r.url} con el código de estado: {r.status_code}")

