#!/usr/bin/env python3

import socket


def start_chat_client():

    host = 'localhost'
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:

        client_msg = input(f"\n[+] Mensaje para enviar al servidor: ")
        client_socket.send(client_msg.encode())

        if client_msg == "bye":
            break

        server_msg = client_socket.recv(1024).strip().decode()
        print(f"\n[+] Mensaje del servidor: {server_msg}")

    client_socket.close()


start_chat_client()
