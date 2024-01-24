#!/usr/bin/env python3
"""
Calculadora
"""

import tkinter as tk


class Calculadora:
    """
    Clase calculadora
    """

    def __init__(self, master):

        self.master = master
        self.display = tk.Entry(
            master, width=20, font=("Arial", 23), justify="right",
            bd=10, insertwidth=1, bg="#6495DE"
        )
        self.display.grid(row=0, column=0, columnspan=4)
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = 0

        row = 1
        col = 0

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "="
        ]

        for button in buttons:

            self.build_button(button, row, col)

            col += 1

            if col > 3:

                col = 0
                row += 1

            if row == 5:
                col += 2

        self.master.bind("<Key>", self.key_press)

    def key_press(self, event):

        key = event.char

        if key in "0123456789.+-*/":

            self.click(key)

        elif key == "\r":

            self.calculate()

        elif key == "\x08":

            self.clear_display()

        elif key == "\x1b":

            self.master.quit()
            return

        else:

            print(f"\n[+] Tecla presionada: {key}")
            print(f"[+] Valor actual: {self.current}")
            print(f"[+] Verificación de operador: {self.op_verification}")
            print(f"[+] Operador: {self.op}")
            print(f"[+] Total: {self.total}")

    def clear_display(self):

        self.display.delete(0, tk.END)
        self.op_verification = False
        self.current = ''
        self.op = ''
        self.total = 0

    def calculate(self):

        if self.current and self.op:

            if self.op == "+":

                self.total += float(self.current)

            elif self.op == "-":

                self.total -= float(self.current)

            elif self.op == "*":

                self.total *= float(self.current)

            elif self.op == "/":

                self.total /= float(self.current)

            self.display.delete(0, "end")
            self.display.insert(tk.END, round(self.total, 3))

        return self.total

    def click(self, key):

        if self.op_verification:

            self.op_verification = False

        self.display.insert(tk.END, key)

        if key in "0123456789" or key == ".":

            self.current += key

        else:

            if self.current:

                if not self.op:

                    self.total = float(self.current)

            self.current = ''

            self.op_verification = True
            self.op = key

        print(f"\n[+] Tecla presionada: {key}")
        print(f"[+] Valor actual: {self.current}")
        print(f"[+] Verificación de operador: {self.op_verification}")
        print(f"[+] Operador: {self.op}")
        print(f"[+] Total: {self.total}")

    def build_button(self, button, row, col):

        if button == "C":

            b = tk.Button(
                self.master, text=button,
                width=3,
                font=("Arial", 23),
                command=lambda: self.clear_display()
            )

        elif button == "=":

            b = tk.Button(
                self.master, text=button,
                width=8, height=2,
                font=("Arial", 23),
                command=lambda: self.calculate()
            )

        else:

            b = tk.Button(
                self.master, text=button,
                width=3,
                font=("Arial", 23),
                command=lambda: self.click(button)
            )

        b.grid(row=row, column=col, columnspan=2 if row == 5 else 1)


root = tk.Tk()
root.title("Calculadora")
root.resizable(width=False, height=False)
my_gui = Calculadora(root)

root.mainloop()
