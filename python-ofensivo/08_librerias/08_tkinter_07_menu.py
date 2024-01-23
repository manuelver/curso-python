#!/usr/bin/env python3
"""
Librería tkinter - Menu() Widget

"""

import tkinter as tk
from tkinter import messagebox as mb

def accion_menu():
    mb.showinfo("Información", "Este texto forma parte de un menú de opciones")

root = tk.Tk()
root.geometry("300x300")
root.title("Menu() Widget")

# Crear un menú
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu1 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Menú", menu=menu1)

menu1.add_command(label="Opción 1")
menu1.add_command(label="Opción 2")

menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu2)

menu2.add_command(label="Acerca de...", command=accion_menu)

root.mainloop()
