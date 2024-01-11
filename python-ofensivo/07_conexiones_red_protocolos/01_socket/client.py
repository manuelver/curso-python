#!/usr/bin/env python3
"""
Client socket

Con errores. 02_socket es la versión corregida.
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
client_socket.connect(server_address)

try:

    message = b"Ola k ase servidor"
    client_socket.sendall(message)
    data = client_socket.recv(1024)
    print(f"[i] Mensaje de {server_address}:\n\t{data.decode()}")

finally:

    client_socket.close()
