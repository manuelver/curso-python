#!/usr/bin/env python3

import socket


def start_chat_server():
    host = 'localhost'
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # reuse socket TIME_WAIT
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"\n[+] Servidor listo para aceptar una conexión en {host}:{port}")

    conn, addr = server_socket.accept()

    print(f"\n[+] Conexión establecida con {addr[0]}:{addr[1]}")

    while True:

        client_msg = conn.recv(1024).strip().decode()
        print(f"\n[+] Mensaje del cliente: {client_msg}")

        if client_msg == "bye":
            break

        server_msg = input(f"\n[+] Mensaje para el cliente: ")
        conn.send(server_msg.encode())

    print(f"\n[+] Conexión finalizada con {addr[0]}:{addr[1]}")
    conn.close()


start_chat_server()
