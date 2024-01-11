#!/usr/bin/env python3
"""
Servidor UDP
"""


import socket

def start_udp_server():

    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Servidor UDP escuchando en {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"Recibido {data.decode()} de {addr}")
            s.sendto(data, addr)

start_udp_server()