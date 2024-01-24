#!/usr/bin/env python3
"""
Librería tkinter - messagebox

Con dir(messagebox) podemos ver los métodos que tiene esta librería

"""

import tkinter as tk
from tkinter import messagebox as mb


def accion_boton():
    mb.showinfo("Información",
                "Este texto ha salido porque has pulsado el botón")


root = tk.Tk()
root.geometry("150x80")
root.title("Button() Widget & messagebox")

boton = tk.Button(root, text="ClickMe", command=accion_boton)
boton.pack(pady=10)

root.mainloop()
