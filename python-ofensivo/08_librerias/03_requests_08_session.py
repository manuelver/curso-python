#!/usr/bin/env python3

import requests

url = 'https://httpbin.org/cookies'
set_cookies_url = 'https://httpbin.org/cookies/set/my_cookie/123123'

# Crear una sesión para arrastrar la cookie
s = requests.Session()

response = s.get(set_cookies_url)
response = s.get(url)

print(response.text)

