#!/usr/bin/env python3
"""
CLIENTE DE CHAT CIFRADO E2E
"""

import ssl
import socket as s
import threading as th
from tkinter import *
from tkinter.scrolledtext import ScrolledText


def send_message(client_socket, username, text_widget, entry_widget):

    local_address = client_socket.getsockname()
    ip_address, port = local_address

    message = entry_widget.get()
    client_socket.sendall(
        f'{username} ({ip_address}:{port}): {message}\n'.encode())

    entry_widget.delete(0, END)
    text_widget.configure(state='normal')
    text_widget.insert(END, f'{username} ({ip_address}:{port}): {message}\n')
    text_widget.configure(state='disabled')


def receive_message(client_socket, text_widget):

    while True:

        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            text_widget.configure(state='normal')
            text_widget.insert(END, message)
            text_widget.configure(state='disabled')

        except:
            break


def list_users_request(client_socket):

    client_socket.sendall("!usuarios".encode())


def exit_request(client_socket, username, window):

    client_socket.sendall(
        f"\n[!] El usuario {username} ha abandonado el chat\n".encode()
    )
    client_socket.close()

    window.quit()
    window.destroy()


def client_program():

    host = 'localhost'
    port = 1234

    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket = ssl.wrap_socket(client_socket)
    client_socket.connect((host, port))

    username = input("\n[+] Introduce tu usuario: ")

    if not username:
        username = "Anonymus"

    client_socket.sendall(username.encode())

    window = Tk()
    window.title(f'Chat cifrado E2E - {username}')

    text_widget = ScrolledText(window, state='disabled')
    text_widget.pack(padx=5, pady=5)

    frame_widget = Frame(window)
    frame_widget.pack(fill=BOTH, expand=True, padx=5, pady=5)

    entry_widget = Entry(frame_widget, font=('Arial', 12))
    entry_widget.bind(
        "<Return>",
        lambda _: send_message(
            client_socket, username,
            text_widget, entry_widget
        )
    )
    entry_widget.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

    button_widget = Button(
        frame_widget, text="Enviar",
        command=lambda: send_message(
            client_socket, username,
            text_widget, entry_widget
        )
    )
    button_widget.pack(side=RIGHT, padx=5, pady=5)

    users_widget = Button(
        window, text="Listar usuarios",
        command=lambda: list_users_request(client_socket))
    users_widget.pack(padx=5, pady=5)

    exit_widget = Button(
        window, text="Salir",
        command=lambda: exit_request(client_socket, username, window))
    exit_widget.pack(padx=5, pady=5)

    thread = th.Thread(
        target=receive_message,
        args=(client_socket, text_widget)
    )
    thread.daemon = True
    thread.start()

    window.mainloop()
    client_socket.close()


if __name__ == '__main__':
    client_program()
