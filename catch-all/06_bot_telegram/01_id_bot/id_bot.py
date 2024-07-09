import telebot
import os
from dotenv import load_dotenv

load_dotenv('.env')
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['get_group_id'])
def get_group_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"El ID de este grupo es: {chat_id}")


bot.polling()
