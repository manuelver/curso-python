#!/usr/bin/env python3

import socket


def start_udp_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

        msg = 'Hola Servidor UDP! Se está tensando para pasar tildes'.encode(
            'utf-8')
        s.sendto(msg, (host, port))


start_udp_client()
