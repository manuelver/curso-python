#!/usr/bin/env python3
"""
Librería tkinter - grid

"""

import tkinter as tk

root = tk.Tk()
root.title("Mi primera aplicación gráfica")

label1 = tk.Label(root, text="Hola mundo!", bg="red", fg="white")
label2 = tk.Label(root, text="Segundo Hola mundo!", bg="blue", fg="white")
label3 = tk.Label(root, text="Ola k ase", bg="green", fg="white")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)

root.mainloop()
