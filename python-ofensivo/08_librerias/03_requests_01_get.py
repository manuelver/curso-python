#!/usr/bin/env python3
"""
Documentación Librería requests: https://requests.readthedocs.io/en/latest/
"""

import requests

response = requests.get('https://google.es')

print(f"\n[+] Status code: {response.status_code}")
print(f"\n[+] Headers: {response.headers['content-type']}")
print(f"\n[+] Encoding: {response.encoding}")
print(f"\n[+] Guardando código fuente en index.html")

with open('index.html', 'w') as f:
    f.write(response.text)

# https://httpbin.org/get

values = {'name': 'John Doe', 'age': 22, 'method': 'get'}

response = requests.get('https://httpbin.org/get', params=values)

print(f"\n[+] URL final: {response.url}")
print(f"\n[+] Código fuente: {response.text}")

# https://httpbin.org/post

payload = {'name': 'John Doe', 'age': 22, 'method': 'post'}

response = requests.post('https://httpbin.org/post', params=payload)

print(f"\n[+] URL final: {response.url}")
print(f"\n[+] Código fuente: {response.text}")
