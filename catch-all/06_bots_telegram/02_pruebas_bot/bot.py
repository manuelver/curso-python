"""
Pruebas con un bot de Telegram
Doc: https://github.com/eternnoir/pyTelegramBotAPI
"""
# bot.py
# Este es el script principal que ejecuta el bot de Telegram.

import signal
from termcolor import colored
from handlers import bot
from logger import logger


def def_handler(sig, frame):
    """
    Manejador de señal para cerrar el programa de forma segura.

    Args:
        sig: Señal recibida.
        frame: Frame actual.
    """

    print(colored(
        f"\n\n[!] Saliendo del programa...\n", "red", attrs=["bold"]
    ))
    logger.info("Bot detenido por el usuario.")
    bot.stop_polling()
    exit(1)


# Configurar el manejador de señal para SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, def_handler)


# Iniciar el bot
if __name__ == "__main__":
    try:
        logger.info("Bot iniciado.")
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"Error en la ejecución del bot: {str(e)}")
    except KeyboardInterrupt:
        def_handler(None, None)
