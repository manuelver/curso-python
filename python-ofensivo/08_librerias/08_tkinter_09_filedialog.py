#!/usr/bin/env python3
"""
Librería tkinter - filedialog

"""

import tkinter as tk
from tkinter import filedialog as fd


def abrir_archivo():
    ruta_archivo = fd.askopenfilename()
    print(f"[+] Ruta del archivo seleccionado: {ruta_archivo}")


root = tk.Tk()
root.geometry("150x80")
root.title("Button() Widget & messagebox")

boton = tk.Button(root, text="Abrir archivo", command=abrir_archivo)
boton.pack(pady=10)

root.mainloop()
