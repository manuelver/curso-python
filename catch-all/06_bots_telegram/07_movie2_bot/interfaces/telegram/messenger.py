from telegram.constants import ParseMode
import telegram.ext

class Messenger:
    formats = {
        'regular': "*%s*",
        'caption': "*%s*",
        'title': "=+= *%s* =+=",
        'highlight': "--+ %s +--",
        'bold': "*%s* %s"
    }

    def __init__(self, bot, logger):
        self.logger = logger
        self.logger.debug("Started...")
        self.bot = bot

    def send_msg(self, chat_id, msg, type_msg='regular'):
        if type_msg not in self.formats:
            self.logger.error(f"Invalid message type: {type_msg}")
            return

        formatted_msg = self.format(type_msg, msg)
        try:
            self.bot.send_message(
                chat_id=chat_id,
                text=formatted_msg,
                parse_mode=ParseMode.MARKDOWN_V2
            )
        except Exception as e:
            self.logger.error(f"Error sending message: {e}")

    def format(self, type_msg, msg):
        return self.formats[type_msg] % msg

    def send_photo(self, chat_id, photo, caption):
        try:
            self.bot.send_photo(
                chat_id=chat_id,
                photo=photo,
                caption=caption,
                parse_mode=ParseMode.MARKDOWN_V2
            )
        except Exception as e:
            self.logger.error(f"Error sending photo: {e}")
