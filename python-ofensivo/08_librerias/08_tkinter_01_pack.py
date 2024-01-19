#!/usr/bin/env python3
"""
Librería tkinter - pack

"""

import tkinter as tk


def accion_de_boton():

    print(f"\n[+] Se ha presionado el botón")


root = tk.Tk()
root.title("Mi primera aplicación gráfica")

label1 = tk.Label(root, text="Hola mundo!", bg="red", fg="white")
label2 = tk.Label(root, text="Hola mundo!", bg="blue", fg="white")
label3 = tk.Label(root, text="Hola mundo!", bg="green", fg="white")
label1.pack(fill=tk.X)
label2.pack(fill=tk.X)
label3.pack(side=tk.LEFT, fill=tk.Y)

button1 = tk.Button(root, text="Accion",
                    command=accion_de_boton, bg="grey", fg="white")
button2 = tk.Button(root, text="Salir", command=root.quit,
                    bg="white", fg="black")
button1.pack()
button2.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
