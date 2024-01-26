#!/usr/bin/env/ python3
"""
Escaner de puertos
"""

import socket as s
import os


os.system("clear")
print("""
##################
Escaner de puertos
##################
""")
os.system("sleep 0.6")

host = input("\n[+] Introduce la IP a escanear: ")
port = int(input("[+] Introduce el puerto a escanear: "))

def port_scanner():

    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.settimeout(0.9)

    if not sock.connect_ex((host, port)):
        print(f"[+] El puerto {port} está abierto")
    else:
        print(f"[!] El puerto {port} está cerrado")

    sock.close()


def main():
    port_scanner()


if __name__ == "__main__":
    main()
