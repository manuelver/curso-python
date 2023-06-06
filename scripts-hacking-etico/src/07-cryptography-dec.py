"""
Desencriptar mensaje anterior
"""

from cryptography.fernet import Fernet

key = b'GccwcTdrJaoP7z26l2rZHAITi7CZrreIAqwb3X2Lq8s=NO'

# Crear un objeto Fernet con la clave
cipher = Fernet(key)

# Mensaje encriptado
encrypted_message = b'gAAAAABkf4K73Fl-2ZZlYkVhntF5YPcjIXx3zSkYx2lKdpxh5r8nv0zpBLOOtzCkOxMjX8mSx18hMbV5AwZZg1HAJKOskntvBAyiQmqtXbHLe18L5tiU2uw='

# Desencriptar el mensaje
decrypted_message = cipher.decrypt(encrypted_message)

# Imprimir el mensaje desencriptado
print(f"Mensaje desencriptado: {decrypted_message}")
