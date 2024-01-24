#!/usr/bin/env python3
"""
Editor de texto simple
"""

import tkinter as tk
from tkinter import filedialog, messagebox


class SimpleTextEditor:

    def __init__(self, root):

        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        self.current_open_file = ""

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_open_file = ""

    def open_file(self):

        filename = filedialog.askopenfilename(
            title="Seleccione un archivo"
        )

        if filename:

            self.text_area.delete("1.0", tk.END)

            with open(filename, 'r') as file:

                self.text_area.insert("1.0", file.read())

            self.current_open_file = filename

    def save_file(self):

        if not self.current_open_file:

            new_file_path = filedialog.asksaveasfilename(
                title="Guardar archivo"
            )

            if new_file_path:

                self.current_open_file = new_file_path

            else:

                return

        with open(self.current_open_file, 'w') as file:

            file.write(self.text_area.get("1.0", tk.END))

    def quit_confirm(self):

        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):

            self.root.destroy()


root = tk.Tk()
root.geometry("900x700")
root.title("Editor de texto simple")

editor = SimpleTextEditor(root)

menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Salir", command=editor.quit_confirm)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)

root.mainloop()
