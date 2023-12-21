#!/usr/bin/env python3
"""
Clase con muchos métodos mágicos de Python
"""


class Persona:

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

    def __add__(self, other):
        return self.edad + other.edad

    def __sub__(self, other):
        return self.edad - other.edad

    def __mul__(self, other):
        return self.edad * other.edad

    def __truediv__(self, other):
        return self.edad / other.edad

    def __floordiv__(self, other):
        return self.edad // other.edad

    def __mod__(self, other):
        return self.edad % other.edad

    def __pow__(self, other):
        return self.edad ** other.edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __le__(self, other):
        return self.edad <= other.edad

    def __eq__(self, other):
        return self.edad == other.edad

    def __ne__(self, other):
        return self.edad != other.edad

    def __gt__(self, other):
        return self.edad > other.edad

    def __ge__(self, other):
        return self.edad >= other.edad

    def __len__(self):
        return len(self.nombre)

    def __getitem__(self, item):
        return self.nombre[item]

    def __setitem__(self, key, value):
        self.nombre[key] = value

    def __delitem__(self, key):
        del self.nombre[key]

    def __iter__(self):
        return iter(self.nombre)

    def __contains__(self, item):
        return item in self.nombre

    def __call__(self, *args, **kwargs):
        print("Estoy llamando a la clase Persona")

    def __enter__(self):
        print("Entrando a la clase Persona")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo de la clase Persona")

    def __del__(self):
        print("Borrando la clase Persona")

    def __new__(cls, *args, **kwargs):
        print("Creando la clase Persona")
        return super().__new__(cls)

    def __hash__(self):
        return hash(self.nombre)

    def __copy__(self):
        return Persona(self.nombre, self.edad)

    def __deepcopy__(self, memodict={}):
        return Persona(self.nombre, self.edad)

    def __format__(self, format_spec):
        return f"{self.nombre} tiene {self.edad} años"

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __delattr__(self, item):
        super().__delattr__(item)

    def __dir__(self):
        return super().__dir__()

    def __reversed__(self):
        return reversed(self.nombre)

    def __reduce__(self):
        return self.nombre, self.edad

    def __reduce_ex__(self, protocol):
        return self.nombre, self.edad

    def __sizeof__(self):
        return super().__sizeof__()

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

