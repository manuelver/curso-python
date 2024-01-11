#!/usr/bin/env python3
"""
Servidor socket

Con errores. 02_socket es la versión corregida.
"""

import socket

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlazar el socket con el puerto
server_address = ("localhost", 1234)
# Asignar una dirección y un puerto al socket
server_socket.bind(server_address)
# Limitar el número de conexiones entrantes
server_socket.listen(1)

# Esperar a que lleguen conexiones
while True:

    print("  Esperando conexión...")
    # Aceptar una conexión
    client_socket, client_address = server_socket.accept()
    # Formato de datos recibidos
    data = client_socket.recv(1024)

    # Imprimir información de la conexión
    print(f"[+] Cliente conectado desde: {client_address}")
    # Imprimir datos recibidos
    print(f"[i] Mensaje de {client_address}:\n\t{data.decode()}")

    # Enviar datos a cliente
    client_socket.sendall(f"Ola k ase client\n".encode())

    print("[!] Conexión cerrada")
    client_socket.close()

    server_socket.close()
