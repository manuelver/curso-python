"""
Instalar la biblioteca de Python `python-nmap` 
y realizar un escaneo de puertos 
a la dirección IP `192.168.1.1`
"""

import nmap

# Crear un objeto de escaner de puertos
scanner = nmap.PortScanner()

# Escanear los puertos en la dirección IP
result = scanner.scan('192.168.1.1', '1-1000')

# Imprimir los resultados del escaneo

for port in result['scan']['192.168.1.1']['tcp']:
    state = result['scan']['192.168.1.1']['tcp'][port]['state']

    print(f'Puerto {port} está {state}')
