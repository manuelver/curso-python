#!/usr/bin/env python3

import requests

# htpps://httpbin.org/basic-auth/foo/bar

# Con with arrastramos una sesión
with requests.Session() as session:

    session.auth = ('foo', 'bar')
    response1 = session.get('https://httpbin.org/basic-auth/foo/bar')
    print(response1.text)

    # En la segunda sesión estaremos autenticados
    response2 = session.get('https://httpbin.org/basic-auth/foo/bar')
    print(response2.text)
    
