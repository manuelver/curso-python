"""
# Ejemplo de uso del logger

if __name__ == "__main__":
    logger.info('Logger configurado correctamente.')
    logger.debug('Este es un mensaje de depuración.')
    logger.warning('Este es un mensaje de advertencia.')
    logger.error('Este es un mensaje de error.')
    logger.critical('Este es un mensaje crítico.')
"""

# logger.py
# Este módulo configura el logging con rotación de archivos.


import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger():
    # Crear el directorio de logs si no existe
    log_directory = 'logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Ruta del archivo de log
    log_file = os.path.join(log_directory, 'bot.log')

    # Formato de los mensajes de log
    log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Configurar RotatingFileHandler
    # maxBytes: tamaño máximo del archivo de log en bytes (5MB en este caso)
    # backupCount: número máximo de archivos de respaldo
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    # Configurar StreamHandler para la consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    # Puedes cambiar este nivel según tus necesidades
    console_handler.setLevel(logging.DEBUG)

    # Configurar el logger
    logger = logging.getLogger('telegram_bot')
    # Configurar el nivel del logger a DEBUG para capturar todos los mensajes
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Evitar que los mensajes se dupliquen en el log
    logger.propagate = False

    return logger


# Inicializar el logger
logger = setup_logger()
