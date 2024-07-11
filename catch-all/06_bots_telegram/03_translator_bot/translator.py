"""
Este módulo contiene el código para un bot de Telegram que realiza tareas de traducción.

El bot utiliza la API de Telegram Bot para interactuar con los usuarios y la API de Google Translate para la traducción.

La función principal inicializa el bot y comienza a escuchar los mensajes entrantes.

Para ejecutar el bot, asegúrese de tener las credenciales y la configuración de la API necesarias configuradas en el módulo `config`.

Extraido del tutorial de youtube y luego actualizado: https://www.youtube.com/watch?v=8buZAq148gk&ab_channel=SBDeveloper

Autor: manuelver
"""

import signal

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, CallbackContext, filters, CallbackQueryHandler

from translate import Translator

import config
from logger import logger


def def_handler(sig, frame):
    """
    Función manejadora de señales para salir del programa de manera elegante.
    """
    logger.info("Saliendo del programa...")
    exit(1)


# Configurar el manejador de señal para SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, def_handler)


async def select_origin_lang(update: Update, context: CallbackContext) -> None:
    """
    Función para seleccionar el idioma de origen para la traducción.
    """
    keyboard = [
        [
            InlineKeyboardButton("Español", callback_data='es'),
            InlineKeyboardButton("Catalán", callback_data='ca'),
            InlineKeyboardButton("English", callback_data='en'),
            InlineKeyboardButton("Français", callback_data='fr')
        ],
        [
            InlineKeyboardButton("Deutsch", callback_data='de'),
            InlineKeyboardButton("Italiano", callback_data='it'),
            InlineKeyboardButton("Português", callback_data='pt')
        ],
        [
            InlineKeyboardButton("Русский (Ruso)", callback_data='ru'),
            InlineKeyboardButton("日本語 (Japonés)", callback_data='ja'),
            InlineKeyboardButton("中文 (Chino)", callback_data='zh')
        ],
        [
            InlineKeyboardButton("(Árabe) العربية", callback_data='ar'),
            InlineKeyboardButton("हिन्दी (Hindi)", callback_data='hi'),
            InlineKeyboardButton("עברית (Hebreo)", callback_data='he')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        'Por favor, selecciona el idioma de origen:', reply_markup=reply_markup)


async def select_dest_lang(update: Update, context: CallbackContext) -> None:
    """
    Función para seleccionar el idioma de destino para la traducción.
    """
    keyboard = [
        [
            InlineKeyboardButton("Español", callback_data='es'),
            InlineKeyboardButton("Catalán", callback_data='ca'),
            InlineKeyboardButton("English", callback_data='en'),
            InlineKeyboardButton("Français", callback_data='fr')
        ],
        [
            InlineKeyboardButton("Deutsch", callback_data='de'),
            InlineKeyboardButton("Italiano", callback_data='it'),
            InlineKeyboardButton("Português", callback_data='pt')
        ],
        [
            InlineKeyboardButton("Русский (Ruso)", callback_data='ru'),
            InlineKeyboardButton("日本語 (Japonés)", callback_data='ja'),
            InlineKeyboardButton("中文 (Chino)", callback_data='zh')
        ],
        [
            InlineKeyboardButton("(Árabe) العربية", callback_data='ar'),
            InlineKeyboardButton("हिन्दी (Hindi)", callback_data='hi'),
            InlineKeyboardButton("עברית (Hebreo)", callback_data='he')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f'Por favor, selecciona el idioma de destino:', reply_markup=reply_markup)



async def button(update: Update, context: CallbackContext) -> None:
    """
    Función para manejar los botones de idioma seleccionados.
    """
    query = update.callback_query
    await query.answer()

    if 'origin_lang' not in context.user_data:
        context.user_data['origin_lang'] = query.data
        await query.edit_message_text(text=f"Idioma de origen seleccionado.\n\nAhora selecciona el idioma de destino con el comando /langTo")
        await select_dest_lang(update, context)
    else:
        context.user_data['dest_lang'] = query.data
        await query.edit_message_text(text=f"Idioma de destino seleccionado.\n\nEnvía tu texto para traducir.")

    logger.info(f"Idioma seleccionado: {query.data}")


async def lang_translator(user_input, from_lang, to_lang):

    try:
        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        translation = translator.translate(user_input)

        return translation

    except TranslationError as e:
        logger.error(f"Error en la traducción: {str(e)}")
        return "Error en la traducción. Por favor, intenta de nuevo más tarde."

    except Exception as e:
        logger.error(f"Error inesperado al traducir el texto: {str(e)}")
        return "Error inesperado al traducir el texto."


async def reply(update: Update, context: CallbackContext):

    user_input = update.message.text
    from_lang = context.user_data.get(
        'origin_lang', 'es')  # Español por defecto
    to_lang = context.user_data.get('dest_lang', 'en')  # Inglés por defecto

    translation = await lang_translator(user_input, from_lang, to_lang)
    await update.message.reply_text(translation)

    logger.info(f"Mensaje recibido: {user_input}")
    logger.info(f"Texto traducido: {translation}")


async def start(update: Update, context: CallbackContext):

    await update.message.reply_text("¡Hola! Soy un bot de traducción.\n\nSi necesitas ayuda: /help.")

    logger.info("Comando /start recibido.")


async def help_command(update: Update, context: CallbackContext):
    """
    Función para mostrar los comandos disponibles.
    """
    commands = [
        "/start - Iniciar el bot",
        "/langFrom - Seleccionar idioma de origen",
        "/langTo - Seleccionar idioma de destino",
        "/help - Mostrar este mensaje de ayuda"
    ]
    help_text = "\n".join(commands)

    await update.message.reply_text(f"El idioma por defecto origen es español y el de destino el Inglés.\nPuedes configurar otras opciones.\nUna vez lo tengas listo tan solo tienes que enviar el texto con el idioma origen.\n\nOpciones:\n{help_text}")

    logger.info("Comando /help recibido.")


def main():
    """
    Función principal para inicializar el bot y comenzar a escuchar los mensajes.
    """
    api = config.BOT_TOKEN

    application = ApplicationBuilder().token(api).build()

    # Manejadores de comandos y mensajes
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('langFrom', select_origin_lang))
    application.add_handler(CommandHandler('langTo', select_dest_lang))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('command', help_command))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, reply))
    application.add_handler(CallbackQueryHandler(button))

    # Iniciar el bot
    logger.info("Bot iniciado.")

    # Iniciar el bucle de eventos
    application.run_polling()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(f'Error en la ejecución del bot: {str(e)}')
    except KeyboardInterrupt:
        def_handler(None, None)
