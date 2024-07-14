# config.py
# Este módulo gestiona la configuración y la carga de variables de entorno.

import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv('.env')

# Obtener el token del bot y el ID del chat de grupo desde las variables de entorno
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Validar que las variables de entorno estén configuradas
if not BOT_TOKEN or not WEATHER_API_KEY:
    raise AssertionError("Por favor, configura las variables de entorno BOT_TOKEN y GROUP_CHAT_ID")

