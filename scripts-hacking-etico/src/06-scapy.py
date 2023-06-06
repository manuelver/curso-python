"""
Instalar la biblioteca de Python `scapy` 
y crear un paquete de red personalizado 
que contenga un mensaje de texto
"""
from scapy.all import *

# Crear un paquete IP con un mensaje de texto
packet = IP(dst="192.168.1.1")/ICMP()/"Hola, este es un mensaje de prueba"

# Enviar el paquete
send(packet)
