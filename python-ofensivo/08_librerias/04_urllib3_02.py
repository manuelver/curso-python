#!/usr/bin/env python3
"""
urllin3 

Deshabilitar advertencias de certificado SSL

"""

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_NONE') # Controlador de conexiones

r = http.request(
    'GET', 
    'https://157.240.254.12/', 
)

print(r.data.decode())
