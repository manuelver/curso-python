"""
Instalar la biblioteca de Python `pwntools` 
y crear un exploit que permita a un usuario 
ejecutar comandos en un servidor remoto.
"""
from pwn import *

# Conexión al servidor remoto
conn = remote('192.168.1.1', 80)

# Envío de comandos al servidor
conn.sendline('ls')
conn.sendline('whoami')

# Recibir y mostrar la salida del servidor
output = conn.recvall().decode('latin-1', errors='ignore')
print(output)

# Cerrar la conexión
conn.close()
