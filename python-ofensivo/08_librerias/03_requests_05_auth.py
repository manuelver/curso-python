#!/usr/bin/env python3

import requests

# from requests.auth import HTTPBasicAuth
# Con esta librería se podría detallar el método llamándolo así:
# auth=HTTPBasicAuth('foo', 'bar')

# Paǵina para practicar autenticación: https://httpbin.org/basic-auth/foo/bar

response  = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))

print(f"\n[+] Código de error: {response.status_code}\n")
print(response.text)

