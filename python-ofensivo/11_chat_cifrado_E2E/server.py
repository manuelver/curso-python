#!/usr/bin/env python3
"""
SERVER DE CHAT CIFRADO E2E
"""

import socket as s
import threading as th
import ssl


def client_thread(client_socket, clients, usernames):

    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username

    print(f"\n[+] El usuario {username} se ha conectado al chat")

    for client in clients:
        if client is not client_socket:
            client.sendall(
                f"\n[+] El usuario {username} se ha conectado al chat\n\n".encode()
            )

    while True:

        try:

            message = client_socket.recv(1024).decode()

            if not message:
                break

            if message == "!usuarios":
                client_socket.sendall(
                    f"\n[i] Usuarios conectados: {', '.join(usernames.values())}\n\n".encode()
                )
                continue

            for client in clients:
                if client is not client_socket:
                    client.sendall(message.encode())

        except:
            break

    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]


def server_program():

    host = 'localhost'
    port = 1234

    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)  # TIME_WAIT
    server_socket.bind((host, port))
    server_socket = ssl.wrap_socket(
        server_socket, keyfile='server-key.key', 
        certfile='server-cert.pem', server_side=True
    )
    server_socket.listen()

    print(f"\n[+] Server está en escucha...")

    clients = []
    usernames = {}

    while True:

        client_socket, addr = server_socket.accept()
        clients.append(client_socket)

        print(f"\n[+] Conectado a {addr}")

        thread = th.Thread(
            target=client_thread,
            args=(client_socket, clients, usernames)
        )
        thread.daemon = True
        thread.start()

    server_socket.close()


if __name__ == '__main__':
    server_program()
