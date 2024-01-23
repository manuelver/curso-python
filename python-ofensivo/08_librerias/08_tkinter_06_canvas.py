#!/usr/bin/env python3
"""
Librería tkinter - Canvas() Widget

"""

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Canvas() Widget")

# Crear un Canvas
canvas = tk.Canvas(root, width=250, height=250, bg="white")
canvas.pack(pady=20)

oval = canvas.create_oval(10, 10, 100, 100, fill="red")

rect = canvas.create_rectangle(150, 100, 240, 10, fill="blue")

line = canvas.create_line(10, 200, 100, 220, width=3, fill="green")

root.mainloop()
