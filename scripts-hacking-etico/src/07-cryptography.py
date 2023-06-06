"""
Instalar la biblioteca de Python `cryptography`
y encriptar un mensaje.
"""
from cryptography.fernet import Fernet

# Generar una clave de cifrado
key = Fernet.generate_key()

print(f"Clave de cifrado generada: {key}")

# O utilizar una clave de cifrado ya generada

# key = b'Qd4u32ZW-C3DlWs35tvhgiPUHYP4YmlAfUBAV9EFlBs='

# Crear un objeto Fernet con la clave generada
cipher = Fernet(key)

# Mensaje a encriptar
message = b"Hola, este es un mensaje"

# Encriptar el mensaje
encrypted_message = cipher.encrypt(message)

# Imprimir el mensaje encriptado
print(f"Mensaje encriptado: {encrypted_message}")
