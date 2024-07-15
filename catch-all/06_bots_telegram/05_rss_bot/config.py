# config.py
# Este módulo gestiona la configuración y la carga de variables de entorno.

import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv('.env')

# Obtener el token del bot y el ID del chat de grupo desde las variables de entorno
Token = os.getenv('BOT_TOKEN')
chatid = os.getenv('GROUP_CHAT_ID')

# Este es el retraso entre cada sondeo a las fuentes RSS en segundos.
delay = 30

# Validar que las variables de entorno estén configuradas
if not Token or not chatid:
    raise AssertionError("Por favor, configura las variables de entorno BOT_TOKEN y GROUP_CHAT_ID")

# Convertir GROUP_CHAT_ID a entero
chatid = int(chatid)
