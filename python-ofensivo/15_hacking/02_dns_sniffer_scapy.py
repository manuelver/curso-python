# /usr/bin/env python3
"""
DNS sniffer
"""

import argparse
import signal
import scapy.all as scapy


def def_handler(sig, frame):

    print("\n\n[!] Saliendo del programa...\n")
    exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    """
    Obtiene los argumentos de la línea de comandos
    """

    parser = argparse.ArgumentParser(description="DNS sniffer")
    parser.add_argument(
        "-i", "--interface",
        required=True, dest="interface",
        help="Interfaz de red a utilizar"
    )
    args = parser.parse_args()

    return args


def process_sniffed_packet(packet):
    """
    Procesa el paquete sniffado
    """

    if packet.haslayer(scapy.DNSQR):

        domain = packet[scapy.DNSQR].qname.decode()

        exclude_keywords = ["bing", "google", "static", "cloud", "yahoo"]

        if domain not in domains_seen and not any(keyword in domain for keyword in exclude_keywords):

            domains_seen.add(domain)
            print(f"[+] Dominio: {domain}")


def sniff(interface):
    """
    Sniffing de paquetes
    """

    print("\n[+] Interceptando paquetes de la máquina victima: \n")

    scapy.sniff(
        iface=interface, filter="udp and port 53",
        store=False, prn=process_sniffed_packet
    )


def main():
    """
    Función principal
    """

    arguments = get_arguments()

    sniff(arguments.interface)


if __name__ == "__main__":

    global domains_seen
    domains_seen = set()

    main()
