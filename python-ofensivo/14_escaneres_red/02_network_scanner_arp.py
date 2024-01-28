# /usr/bin/env python3
"""
Escaner de red ARP
"""

import scapy.all as scapy
import argparse


def get_arguments():
    """
    Obtiene los argumentos de la línea de comandos
    """

    parser = argparse.ArgumentParser(description='Escaner de red ARP')
    parser.add_argument(
        '-t', '--target',
        required=True, dest='target',
        help='Host / IP range. ex: 192.168.1.1 or 192.168.1.0/24'
    )
    args = parser.parse_args()

    return args.target


def scan(ip):
    """
    Escanea la red en busca de hosts
    """

    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_packet = broadcast_packet/arp_packet  # / es un operador de composición

    answered, unanswered = scapy.srp(arp_packet, timeout=1, verbose=False)

    response = answered.summary()

    if response:
        print(response)

def main():
    """
    Función principal
    """

    target = get_arguments()
    scan(target)


if __name__ == '__main__':
    main()
