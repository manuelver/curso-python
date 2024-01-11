#!/usr/bin/env python3

import socket
import threading
import pdb


class ClientThread(threading.Thread):

    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

        print(f"\nConexión establecida desde {self.addr}")

    def run(self):
        msg = ''

        while True:

            data = self.conn.recv(1024)
            msg = data.decode()

            # pdb.set_trace() # Breakpoint

            if msg.strip() == 'bye':
                break

            print(f"\n[+] Recibido del cliente {self.addr}: {msg.strip()}")
            self.conn.send(data)

        print(f"\n[-] Cliente {self.addr} desconectado")
        self.conn.close()


HOST = 'localhost'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Alterar propiedades del socket
    # Reutilizar direcciones
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Otras propiedades: https://docs.python.org/3/library/socket.html#socket.socket.setsockopt
    # socket.IPPROTO_IP, socket.IPPROTO_IPV6, socket.IPPROTO_TCP, socket.IPPROTO_UDP...

    # Enlazar socket a dirección y puerto
    s.bind((HOST, PORT))

    print(f"Servidor TCP escuchando en {HOST}:{PORT}")

    while True:

        s.listen()
        conn, addr = s.accept()
        new_thread = ClientThread(conn, addr)
        new_thread.start()
