# handlers.py
# Este módulo contiene los manejadores de mensajes del bot.

from telebot import TeleBot
from logger import logger
import config

# Mensajes de texto del bot en español
text_messages = {
    'welcome':
        u'¡Por favor denle la bienvenida a {name}!\n\n'
        u'Este chat está destinado a preguntas y discusión sobre la pyTelegramBotAPI.\n'
        u'Para permitir que los miembros del grupo respondan a tus preguntas de forma rápida y precisa, asegúrate de '
        u'estudiar la documentación del proyecto (https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md) '
        u'y los ejemplos (https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) primero.\n\n'
        u'¡Espero que disfrutes tu estadía aquí!',

    'info':
        u'Mi nombre es TeleBot,\n'
        u'Soy un bot que asiste a estas maravillosas personas que crean bots en este chat del grupo de la librería.\n'
        u'Además, todavía estoy en desarrollo. ¡Por favor, mejora mi funcionalidad haciendo una solicitud de pull! '
        u'Las sugerencias también son bienvenidas, solo déjalas en este chat del grupo!',

    'wrong_chat':
        u'¡Hola!\nGracias por probarme. Sin embargo, este bot solo puede usarse en el chat del grupo pyTelegramAPI.\n'
        u'¡Únete a nosotros!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}

# Crear una instancia del bot con el token de configuración
bot = TeleBot(config.BOT_TOKEN)

# Manejador para cuando un nuevo participante se une al chat
@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    try:
        # Obtener el nombre del nuevo participante
        name = message.new_chat_participant.first_name
        if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
            name += f" {message.new_chat_participant.last_name}"

        if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
            name += f" (@{message.new_chat_participant.username})"

        # Enviar mensaje de bienvenida
        bot.reply_to(message, text_messages['welcome'].format(name=name))
    except Exception as e:
        logger.error(f"Error en on_user_joins: {str(e)}")

# Manejador para los comandos /info y /help
@bot.message_handler(commands=['info', 'help'])
def on_info(message):
    try:
        bot.reply_to(message, text_messages['info'])
    except Exception as e:
        logger.error(f"Error en on_info: {str(e)}")

# Manejador para el comando /ping
@bot.message_handler(commands=["ping"])
def on_ping(message):
    try:
        bot.reply_to(message, "¡Sigo vivo y pateando!")
    except Exception as e:
        logger.error(f"Error en on_ping: {str(e)}")


# Manejador para el comando /tq
@bot.message_handler(commands=["tq"])
def on_ping(message):
    try:
        bot.reply_to(message, "¡Te quiero princesa!")
    except Exception as e:
        logger.error(f"Error en on_tq: {str(e)}")


# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def on_start(message):
    try:
        bot.reply_to(message, "¡Bienvenido! Usa /info para más información.")
    except Exception as e:
        logger.error(f"Error en on_start: {str(e)}")

# Listener para registrar todos los mensajes recibidos
def listener(messages):
    for m in messages:
        logger.info(f"Mensaje recibido: {str(m)}")

bot.set_update_listener(listener)
