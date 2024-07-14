import asyncio
import logging
import requests

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext
from telegram.ext import filters

import config

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_API_TOKEN = config.BOT_TOKEN
WEATHER_API_KEY = config.WEATHER_API_KEY
BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}"

city = None


def weather_emoji(description):
    """Devuelve un emoji basado en la descripción del clima."""
    description = description.lower()
    if "clear" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "thunder" in description:
        return "⛈️"
    elif "snow" in description:
        return "❄️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return ""


async def start(update: Update, context: CallbackContext) -> None:
    """Manejador del comando /start. Solicita al usuario la ciudad en la que vive."""
    logger.debug(f"Comando /start recibido de {update.message.chat.username}")
    await update.message.reply_text("¿En qué ciudad vives?")


async def menu(update: Update, context: CallbackContext) -> None:
    """Manejador de mensajes. Muestra un menú con opciones al usuario después de recibir la ciudad."""
    global city
    city = update.message.text
    logger.debug(f"Ciudad recibida: {city}")
    keyboard = [
        [InlineKeyboardButton("Clima Actual", callback_data='current_weather')],
        [InlineKeyboardButton("Pronóstico del Tiempo", callback_data='forecast')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Elige una opción:', reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext) -> None:
    """Manejador de botones. Procesa la opción seleccionada por el usuario."""
    query = update.callback_query
    await query.answer()
    logger.debug(f"Opción seleccionada: {query.data}")

    try:
        if query.data == 'current_weather':
            response = requests.get(BASE_WEATHER_URL.format(city, WEATHER_API_KEY))
            response.raise_for_status()
            data = response.json()
            main = data['main']
            weather_data = data['weather'][0]
            celsius_temp = main['temp'] - 273.15
            emoji = weather_emoji(weather_data['description'])
            message = f"Clima actual en {city} {emoji}:\n"
            message += f"Temperatura: {celsius_temp:.2f}°C\n"
            message += f"Descripción: {weather_data['description'].capitalize()}\n"
            message += f"Humedad: {main['humidity']}%\n"
            await query.edit_message_text(text=message)
        elif query.data == 'forecast':
            response = requests.get(FORECAST_URL.format(city, WEATHER_API_KEY))
            response.raise_for_status()
            data = response.json()
            message = f"Pronóstico del tiempo para {city}:\n"
            for item in data['list'][:5]:
                celsius_temp = item['main']['temp'] - 273.15
                emoji = weather_emoji(item['weather'][0]['description'])
                message += f"\nFecha: {item['dt_txt']} {emoji}\n"
                message += f"Temperatura: {celsius_temp:.2f}°C\n"
                message += f"Descripción: {item['weather'][0]['description'].capitalize()}\n"
            await query.edit_message_text(text=message)
    except requests.RequestException as e:
        logger.error(f"Error al obtener datos del clima: {e}")
        await query.edit_message_text(
            text="No se puede encontrar información meteorológica para esta ciudad. Inténtalo de nuevo.")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        await query.edit_message_text(
            text="Ocurrió un error inesperado. Inténtalo de nuevo más tarde.")


def error(update: Update, context: CallbackContext):
    """Registra errores causados por actualizaciones."""
    logger.warning('La actualización "%s" causó el error "%s"', update, context.error)


def main():
    """Función principal del bot. Configura y ejecuta el bot de Telegram."""
    logger.info("Iniciando el bot...")
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))
    application.add_handler(CallbackQueryHandler(button))

    # Registra todos los errores
    application.add_error_handler(error)

    logger.info("Bot iniciado y en espera de mensajes...")
    application.run_polling()


if __name__ == '__main__':
    main()
