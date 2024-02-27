"""
Acortador de enlaces
"""

import argparse
import json
import regex
import secrets
import string
import signal
import sys

from termcolor import colored


def signal_handler(sig, frame):

    print(colored('\n[!] Saliendo...', 'red'))
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def generar_codigo():

    # Definir caracteres para cadena aleatoria
    alfanumerica = string.ascii_letters + string.digits

    # Generar cadena aleatoria
    codigo = ''.join(secrets.choice(alfanumerica) for i in range(8))

    return codigo


def acortar_url(url):

    codigo = generar_codigo()
    data = []

    with open('codigos.json', 'r') as f:

        data = json.load(f)

    codigo_existe = any(item['codigo'] == codigo for item in data)

    if codigo_existe:
        codigo = generar_codigo()

    with open('codigos.json', 'w') as f:

        data.append(
            {
                'codigo': codigo,
                'url': f"http://localhost:5000/{codigo}",
                'redireccion': url,
            }
        )

        json.dump(data, f, indent=4)


def comprobar_url(url):

    # Comprobar si la URL tiene http o https
    if not url.startswith('http://') and not url.startswith('https://'):
        url = f'https://{url}'

    if url.endswith('/'):
        url = url[:-1]

    # Comprobar formato de URL con los patrones
    if regex.match(r'^https?://[\w.-]+\.[\w.-]+(/[\w.-]+)*$', url):

        return url

    else:

        raise ValueError(colored('URL no válida', 'red'))


def main():

    try:
        parser = argparse.ArgumentParser(description='Acortador de URL')
        parser.add_argument('-u', '--url', help='URL a acortar')
        args = parser.parse_args()
        url = args.url

        if not url:

            url = input(colored('Introduce la URL a acortar: ', 'cyan'))

        url = comprobar_url(url)

        acortar_url(url)

    except argparse.ArgumentError as e:
        print(colored(f'[!] Error en los argumentos: {e}', 'red'))

    except Exception as e:
        print(colored(f'[!] Error en la ejecución principal: {e}', 'red'))


if __name__ == "__main__":

    main()
