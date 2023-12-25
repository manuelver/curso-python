#!/usr/bin/env python3
"""
Métodos especiales 
"""


class Pizza:

    def __init__(self, size, *toppings):

        self.size = size
        self.toppings = toppings

    def description(self):

        print(
            f"""
Esta pizza es de {self.size} cm
y tiene los siguientes ingredientes:""")
        for topping in self.toppings:
            print(f"- {topping}")

pizza = Pizza(12, "Chorizo", "Queso", "Jamon", "Cebolla")

pizza.description()
