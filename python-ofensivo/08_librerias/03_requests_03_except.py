#!/usr/bin/env python3

import requests

try:
    response = requests.get('https://google.ese', timeout=1)

    response.raise_for_status()

except requests.Timeout:

    print(f"\n[!] La web ha excedido el límite de tiempo de espera")

except requests.HTTPError as http_err:

    print(f"[!] Error HTTP: {http_err}")


except requests.RequestException as err:

    print(f"\n[!] Error: {err}")

else:

    print(f"\n[+] No ha habido ningún error en la solicitud")

