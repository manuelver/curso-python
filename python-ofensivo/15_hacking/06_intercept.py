#!/usr/bin/env python3

import scapy.all as scapy


def process_packet(packet):
    """
    Procesa los paquetes que llegan a la cola 0
    """

    if packet.haslayer(scapy.DNSRR):

        qname = packet[scapy.DNSQR].qname

        # print(qname)

        if "hack4u.io" in qname.decode() or "vergaracarmona.es" in qname.decode():

            print(
                f"\n------------------\n{packet.show()}\n------------------\n"
            )


scapy.sniff(
    iface="wlo1", filter="udp and port 53",
    store=False, prn=process_packet
)
