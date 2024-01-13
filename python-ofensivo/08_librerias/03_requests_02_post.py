#!/usr/bin/env python3
"""
Documentación Librería requests: https://requests.readthedocs.io/en/latest/
"""

import requests


# https://httpbin.org/post

payload = {'name': 'John Doe', 'age': 22, 'method': 'post'}
headers = {'User-Agent': 'my-invent-app/1.1.0'}
response = requests.post('https://httpbin.org/post', params=payload, headers=headers)

print(f"\n[+] URL final: {response.url}")
print(f"\n[+] Código fuente: {response.text}")
