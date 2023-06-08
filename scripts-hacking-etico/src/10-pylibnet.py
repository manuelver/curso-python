"""
instalar la biblioteca de Python `pylibnet` y 
crear un paquete de red personalizado 
que contenga un mensaje de texto.
"""
from scapy.all import *

# Crear un paquete Ethernet
packet = Ether()

# Definir la dirección MAC de origen y destino
src_mac = "00:11:22:33:44:55"
dst_mac = "AA:BB:CC:DD:EE:FF"

# Definir el mensaje de texto
message = "Hola, este es un mensaje"

# Construir el paquete Ethernet
packet.src = src_mac
packet.dst = dst_mac
packet.type = 0x0800  # Tipo de protocolo IP
packet.payload = message

# Enviar el paquete
sendp(packet)
