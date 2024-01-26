#!/usr/bin/env python3
"""
Cambiar la dirección mac

"""


import argparse
import re
import signal
import subprocess
import sys
from termcolor import colored


def def_handler(sig, frame):

        print(colored(
            f'\n[!] Saliendo del programa...', 'red'
        ))

        sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():

    parser = argparse.ArgumentParser(
        description='Herramienta para cambiar la dirección mac'
    )
    parser.add_argument(
        '-i', '--interface',
        dest='interface',
        help='Nombre de la interfaz de red',
        required=True
    )
    parser.add_argument(
        '-m', '--mac',
        dest='new_mac',
        help='Nueva dirección mac',
        required=True
    )

    return parser.parse_args()


def is_valid_input(interface, new_mac):

    is_valid_interface = re.match(
        r'^[w|e][n|l][o]\d{1,2}$', interface
    )

    is_valid_mac = re.match(
        r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', new_mac
    )

    if not is_valid_interface:

        print(colored(
            f'\n[!] El nombre de la interfaz de red no es válida', 'red'
        ))


    if not is_valid_mac:

        print(colored(
            f'\n[!] La dirección mac no es válida', 'red'
        ))


    return is_valid_interface and is_valid_mac


def change_mac_address(interface, new_mac):

    if is_valid_input(interface, new_mac):

        print(colored(
            f'\n[+] Cambiando la dirección mac de {interface} a {new_mac}', 'blue'
        ))

        subprocess.run(["sudo", "ifconfig", interface, "down"])
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.run(["sudo", "ifconfig", interface, "up"])

        print(colored(
            f'\n[+] Dirección mac cambiada correctamente', 'green'
        ))



def main():

    args = get_arguments()
    change_mac_address(args.interface, args.new_mac)


if __name__ == '__main__':

    main()
