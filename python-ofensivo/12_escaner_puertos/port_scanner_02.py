#!/usr/bin/env/ python3
"""
Escaner de puertos
"""

import argparse
import socket as s
import signal
import sys
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

open_sockets = []


def def_handler(sig, frame):
    """
    Función para manejar la señal SIGINT (Ctrl + C).
    """

    print(colored("\n[!] Saliendo...", "blue"))

    for sock in open_sockets:

        sock.close()

    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)  # CTRL + C


def get_arguments():
    """
    Función para obtener los argumentos de la línea de comandos.
    """

    parser = argparse.ArgumentParser(description="Escaner de puertos TCP")
    parser.add_argument(
        "-t", "--target", dest="target", required=True,
        help="IP objetivo a escanear (Ej: -t 192.168.1.1)"
    )
    parser.add_argument(
        "-p", "--port", dest="port", required=True,
        help="""Rango de puertos a escanear
        (Ej: -p 80 or -p 50-100 or -p 80,443,8080)"""
    )
    options = parser.parse_args()

    return options.target, options.port


def port_scanner(port, host):
    """
    Función para escanear un puerto en un host dado.
    """

    with s.socket(s.AF_INET, s.SOCK_STREAM) as sock:

        try:

            sock.settimeout(2)

            open_sockets.append(sock)

            sock.connect((host, port))

            sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            response = sock.recv(1024)
            response = response.decode(errors="ignore").split("\n")

            if response:
                print(
                    colored(
                        f"\n[+] El puerto {port} está abierto", "green"
                    )
                )
                # print(
                #     colored(
                #         f"\t[+] Respuesta del puerto {port}: {response}",
                #         "blue"
                #     )
                # )

                for line in response:
                    print(colored(line, "grey"))

            else:
                print(
                    colored(
                        f"\n[+] El puerto {port} está abierto",
                        "green"
                    )
                )

        except (s.timeout, ConnectionRefusedError):
            pass

        finally:
            sock.close()


def scan_ports(ports, target):
    """
    Función para escanear una lista de puertos en un host dado.
    """

    with ThreadPoolExecutor(max_workers=100) as executor:

        executor.map(lambda port: port_scanner(port, target), ports)


def parse_ports(ports_str):
    """
    Función para analizar la cadena de puertos y devolver una secuencia de puertos.
    """

    if "-" in ports_str:

        start_port, end_port = map(int, ports_str.split("-"))

        return range(start_port - 1, end_port + 1)

    elif "," in ports_str:

        return map(int, ports_str.split(","))

    else:

        return int(ports_str),


def main():
    """
    Función principal del programa.
    """

    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)

    scan_ports(ports, target)


if __name__ == "__main__":
    main()
