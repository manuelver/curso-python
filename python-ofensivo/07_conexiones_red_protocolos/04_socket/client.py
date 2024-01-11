#!/usr/bin/env python3

import socket


def start_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            msg = input("[+] Introduce un mensaje: ")

            s.sendall(msg.encode('utf-8'))

            if msg.strip() == 'bye':
                break

            data = s.recv(1024)

            print(f"\n[+] Mensaje del servidor: {data.decode().strip()}")


start_client()
