#!/usr/bin/env python3
"""
Librería tkinter - Entry() Widget

"""

import tkinter as tk

root = tk.Tk()
root.geometry("500x700")
root.title("Entry() Widget")


def get_data():
    data = entry_widget.get()
    print(f"\n[+] Datos introduccidos por el usuario:\n{data}")


def get_data_text():
    data = text_widget.get("1.0", tk.END)
    print(f"\n[+] Datos introduccidos por el usuario:\n{data}")


entry_widget = tk.Entry(root, width=50, borderwidth=5)
entry_widget.pack(pady=15, padx=20, fill=tk.X)

boton = tk.Button(root, text="Envia datos", command=get_data)
boton.pack(padx=20, fill=tk.X)

# Con text tengo más lineas de escritura
text_widget = tk.Text(root, width=50, borderwidth=5)
text_widget.pack(pady=15, padx=20, fill=tk.X)

boton = tk.Button(root, text="Envia datos de texto", command=get_data_text)
boton.pack(padx=20, fill=tk.X)

root.mainloop()
