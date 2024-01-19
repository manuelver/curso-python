#!/usr/bin/env python3
"""
Librería tkinter - place
geometry

"""

import tkinter as tk


def accion_de_boton():

    print(f"\n[+] Se ha presionado el botón")


root = tk.Tk()
root.geometry("500x400")
root.title("Mi primera aplicación gráfica")

label1 = tk.Label(root, text="Hola mundo!", bg="red", fg="white")
label2 = tk.Label(root, text="Segundo Hola mundo!", bg="blue", fg="white")
label3 = tk.Label(root, text="Ola k ase", bg="green", fg="white")
label1.place(x=20, y=20)
label2.place(relx=0.1, rely=0.8)
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
