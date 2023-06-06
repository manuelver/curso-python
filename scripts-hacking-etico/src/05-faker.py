"""
Instalar la biblioteca de Python `faker` 
y generar 10 nombres aleatorios
"""
from faker import Faker

# Crear un objeto de Faker
fake = Faker()

# Generar 10 nombres aleatorios
for _ in range(10):
    name = fake.name()
    print(name)
