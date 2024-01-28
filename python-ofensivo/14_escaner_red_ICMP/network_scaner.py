# /usr/bin/env python3
"""
Escaner de red ICMP
"""

import argparse
import ipaddress
import re
import signal
import subprocess
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored


def def_handler(sig, frame):

    print(colored(
        "\n\n[!] Saliendo del programa...\n", "blue")
    )
    exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    """
    Obtiene los argumentos de la linea de comandos
    """

    parser = argparse.ArgumentParser(description="Escaner de red ICMP")
    parser.add_argument(
        "-t", "--target",
        required=True, dest="target",
        help="Host o rango de red a escanear"
    )
    args = parser.parse_args()

    return args.target


def validar_ip(target_str):
    """
    Valida si el target es una IP o un rango de IPs
    """

    # Verificar si es un rango de IPs
    rango_match = re.match(
        r'^(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})-(\d{1,3})$', target_str)

    if rango_match:
        ip_inicio = rango_match.group(1)

        ip_fin = int(rango_match.group(2))

        try:
            # Convertir la IP de inicio a un objeto ipaddress
            ipaddress.IPv4Address(ip_inicio)

            # Verificar que el rango sea válido
            if 0 <= ip_fin <= 255:

                # Crear un objeto ipaddress para la IP de inicio
                inicio = ipaddress.IPv4Address(ip_inicio)

                # Crear un objeto ipaddress para la IP de fin
                fin = ipaddress.IPv4Address(
                    ip_inicio.rsplit('.', 1)[0] + '.' + str(ip_fin)
                )

                # Verificar que la IP de inicio sea menor que la IP de fin
                if inicio < fin:

                    print(colored(
                        f"\n[+] Escaneando el rango de IPs: {inicio} - {fin}",
                        "blue")
                    )
                    rango_ips = ipaddress.summarize_address_range(inicio, fin)
                    return rango_ips

                else:

                    print(colored(
                        "\n[!] Error: El rango debe ser de menor a mayor",
                        "red")
                    )
                    return False

            else:

                print(colored(
                    "\n[!] Error: El rango especificado no es válido",
                    "red")
                )
                return False

        except ipaddress.AddressValueError:

            print(colored(
                "\n[!] Error: El rango especificado no son IPs válidas",
                "red")
            )
            return False

    else:

        # Si no es un rango, verificar si es una IP individual
        try:

            ipaddress.IPv4Address(target_str)
            print(colored(
                f"\n[+] Escaneando IP: {target_str}", "blue")
            )
            return target_str

        except ipaddress.AddressValueError:
            print(colored(
                "\n[!] Error: El target especificado no es una IP válida",
                "red")
            )
            return False


def parse_target(target_str):
    """
    Parsea el target y devuelve una lista de IPs
    """

    if "-" in target_str:

        ip_list = target_str.split('-')

        ip_inicio = ip_list[0]
        ip_fin = int(ip_list[1])

        inicio = ipaddress.IPv4Address(ip_inicio)

        fin = ipaddress.IPv4Address(
            ip_inicio.rsplit('.', 1)[0] + '.' + str(ip_fin)
        )

        ips_return = []

        for ip in range(int(ip_inicio.split('.')[3]), ip_fin + 1):

            ip_address = ip_inicio.rsplit('.', 1)[0] + '.' + str(ip)

            ips_return.append(ip_address)

        return ips_return

    else:

        # Si target_str es una IP individual, crear una lista con esa IP
        target_list = [target_str]

        return target_list


def host_discovwery(target):

    try:

        ping = subprocess.run(
            ["ping", "-c", "1", target],
            timeout=1, stdout=subprocess.DEVNULL
        )

        if ping.returncode == 0:

            print(colored(
                f"[+] {target} está activo", "green")
            )

    except subprocess.TimeoutExpired:
        pass


def main():
    """
    Funcion principal
    """

    target_str = get_arguments()

    if not validar_ip(target_str):

        print(colored(
            "\n[!] Introduce un target válido", "red")
        )

        return

    targets = parse_target(target_str)

    with ThreadPoolExecutor(max_workers=50) as executor:

        executor.map(host_discovwery, targets)


if __name__ == "__main__":
    main()
