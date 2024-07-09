# logger.py
# Este módulo configura el logging con rotación de archivos.

import logging
from logging.handlers import RotatingFileHandler

# Ruta del archivo de log
log_file = 'logs/bot.log'

# Formato de los mensajes de log
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar RotatingFileHandler
# maxBytes: tamaño máximo del archivo de log en bytes (5MB en este caso)
# backupCount: número máximo de archivos de respaldo
file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

# Configurar el logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
