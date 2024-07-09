# config.py
# Este módulo gestiona la configuración y la carga de variables de entorno.

import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv('.env')

# Obtener el token del bot y el ID del chat de grupo desde las variables de entorno
BOT_TOKEN = os.getenv('BOT_TOKEN')
GROUP_CHAT_ID = os.getenv('GROUP_CHAT_ID')

# Validar que las variables de entorno estén configuradas
if not BOT_TOKEN or not GROUP_CHAT_ID:
    raise AssertionError("Por favor, configura las variables de entorno BOT_TOKEN y GROUP_CHAT_ID")

# Convertir GROUP_CHAT_ID a entero
GROUP_CHAT_ID = int(GROUP_CHAT_ID)
