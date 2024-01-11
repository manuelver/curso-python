#!/usr/bin/env python3
"""
Client socket

"""

import socket


def start_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((host, port))

        print(f"[*] Conexión establecida con {host}:{port}")

        s.sendall("Ola k ase server!\n".encode())
        data = s.recv(1024)

    print(f"[i] Mensaje de {host}:{port}:\n\t{data.decode()}")


start_client()
