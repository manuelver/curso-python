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

"""

from mitmproxy import http
from mitmproxy import ctx


def request(packet):

    ctx.log.info(f"\n\n[+] URL: {packet.request.url}\n\n")


def response(packet):

    ctx.log.info(f"\n\n[+] Response: {packet.request.url}\n\n")
