#!/usr/bin/env python3
"""
Librería tkinter - Frame() Widget

"""

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Frame() Widget")

# Crear un frame
frame = tk.Frame(root, bg="blue", bd=5, relief=tk.SUNKEN)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label1 = tk.Label(frame, text="Primero y tal", bg="green", fg="white")
label2 = tk.Label(frame, text="Segundo label", bg="red", fg="white")

label1.pack(fill=tk.X)
label2.pack(fill=tk.X)

root.mainloop()
