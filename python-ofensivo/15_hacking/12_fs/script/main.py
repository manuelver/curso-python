
#!/usr/bin/env python3
"""
Fichero principal de la aplicación.
"""

import signal
import sys

from forwardshell import ForwardShell
from termcolor import colored


def def_handler(sig, frame) -> None:

    print(colored("\n[!] Exiting...", "blue"))

    my_forward_shell.remove_data()

    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


if __name__ == '__main__':

    my_forward_shell = ForwardShell()
    my_forward_shell.run()
