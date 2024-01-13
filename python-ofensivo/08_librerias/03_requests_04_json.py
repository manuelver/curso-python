#!/usr/bin/env python3

import requests

response = requests.get('https://httpbin.org/get')

data = response.json()

if 'headers' in data and 'User-Agent' in data['headers']:

    user_agent = data['headers']['User-Agent']

else:

    print(f"\n[!] No existe el campo User-Agent en la respuesta\n")
