#!/usr/bin/env python3
"""
Server socket
"""

import socket


def start_server():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((host, port))
        s.listen(1)
        print(f"[*] Servidor en escucha en {host}:{port}")

        conn, addr = s.accept()
        print(f"[+] {addr} Conectado.")

        with conn:

            print(f"[*] Conexión establecida con {addr}")

            while True:

                data = conn.recv(1024)

                if not data:
                    break

                conn.sendall(data)

                print(f"[i] Mensaje de {addr}:\n\t{data.decode()}")

                conn.sendall(f"Ola k ase client!\n".encode())


start_server()
