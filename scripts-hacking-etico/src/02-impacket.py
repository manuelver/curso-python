"""
Instalar la biblioteca de Python `impacket` 
y realizar un escaneo de puertos 
a la dirección IP `192.168.1.1`
"""
from impacket import smb

# Crear un objeto de cliente SMB
client = smb.SMB('*SMBSERVER', '192.168.1.110')

# Conectar al servidor SMB
client.connect()

# Escanear puertos
ports = client.scan_ports()

# Imprimir puertos abiertos
for port in ports:
    print(f'El puerto {port} está abierto')
