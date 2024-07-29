import logging
from argparse import ArgumentParser
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import conf
import interfaces
import player
import quiz
import session
from translations.required import *


class Server:
    logger = logging.getLogger(__name__)
    SESSIONS = dict()

    def __init__(self):
        self.config_instance = self.config_init()

        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.DEBUG,
            handlers=[
                logging.FileHandler(self.config_instance.LOG_FILE),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger(__name__)

        self.application = Application.builder().token(
            self.config_instance.TELEGRAM_BOT_API).build()

        # Add handlers
        self.application.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND, self.command_check_resps))  # Add handler for non-command messages
        self.application.add_handler(
            CommandHandler('start', self.command_start))
        self.application.add_handler(CommandHandler('roll', self.command_roll))
        self.application.add_handler(CommandHandler(
            "leaderboard", self.command_leaderboard))
        self.application.add_handler(
            CommandHandler("repeat", self.command_repeat))
        self.application.add_handler(CommandHandler("cut", self.command_cut))
        self.application.add_handler(CommandHandler("stop", self.command_stop))
        self.application.add_error_handler(self.error)

        # Set up job queue
        self.application.job_queue.run_repeating(
            self.update_all_timers, interval=60)

        self.logger.info("Iniciando...")

        # Start the Bot
        self.application.run_polling()

    def config_init(self):
        self.logger.info("Config init...")

        arg_parser = ArgumentParser(description="Movie2 Bot")

        arg_parser.add_argument(
            "-e", "--env", metavar="env", type=str, default="prod",
            help="Environment to run the bot: dev, test or prod"
        )

        arg_parser.add_argument(
            "-v", "--verbose", metavar="verbose", type=bool, default=False,
            help="Print information about running bot"
        )

        args = arg_parser.parse_args()

        if args.env == "prod":
            return conf.ProductionConfig()
        elif args.env == "dev":
            return conf.DevelopmentConfig()
        else:
            return conf.TestingConfig()

    async def error(self, update: Update, context: CallbackContext):
        self.logger.warning(
            f'Update "{update}" caused error "{context.error}"')

    async def update_all_timers(self, context: CallbackContext):
        self.logger.info("Updating all timers...")
        for sess in self.SESSIONS.values():
            sess.update_timers()
            if hasattr(sess, 'quiz'):
                sess.quiz.check_expiration()
            else:
                self.logger.error("Quiz class not found in session")

    async def command_start(self, update: Update, context: CallbackContext):
        self.logger.info("Command start...")
        chat_id = update.message.chat_id
        await update.message.reply_text('¡Hola! El comando /start ha sido recibido.')

        if chat_id not in self.SESSIONS:
            self.messenger = interfaces.TelegramMessenger(
                context.bot, self.logger
            )
            self.SESSIONS[chat_id] = session.Session(
                chat_id, self.config_instance, self.logger
            )
            self.SESSIONS[chat_id].set_messenger(self.messenger)

            # Crear una instancia de la clase Quiz
            try:
                self.SESSIONS[chat_id].quiz = quiz.Quiz(self.SESSIONS[chat_id])
            except AttributeError as e:
                self.logger.error(f"Error creating Quiz instance: {e}")
                await self.messenger.send_msg(
                    chat_id, _("error_creating_quiz_instance")
                )
                logging.error(f"Error creating Quiz instance: {e}")

    async def command_roll(self, update: Update, context: CallbackContext):
        self.logger.info("Command roll...")
        chat_id = update.message.chat_id
        args = context.args
        rand_type = args[0] if args else None
        await self.SESSIONS[chat_id].messenger.send_msg(
            chat_id, _("searching_movies"))
        if hasattr(self.SESSIONS[chat_id], 'quiz'):
            await self.SESSIONS[chat_id].quiz.show(update, rand_type)
        else:
            self.logger.error("Quiz instance not found in session")

    async def command_leaderboard(self, update: Update, context: CallbackContext):
        self.logger.info("Command leaderboard...")
        chat_id = update.message.chat_id
        sess = self.SESSIONS.get(chat_id)
        if sess:
            try:
                await sess.messenger.send_msg(
                    chat_id, _("leader_board_title"), 'highlights'
                )
                ldb = sess.get_leaderboard()
                await sess.messenger.send_msg(chat_id, ldb)
            except ValueError as e:
                await sess.messenger.send_msg(
                    chat_id, f'{update.message.from_user.first_name} {e.args[0]}'
                )
        else:
            await update.message.reply_text(_("session_not_found"))

    async def command_action(self, update: Update, context: CallbackContext):
        self.logger.info("Command action...")
        chat_id = update.message.chat_id
        try:
            player = player.Player(update.message.from_user.id)
            player.name = f'{update.message.from_user.first_name} {update.message.from_user.last_name}'
            self.SESSIONS[chat_id].player_add(player)
            await self.SESSIONS[chat_id].messenger.send(
                update, f'{player.name} {_("joined_the_game")}'
            )
        except ValueError as e:
            await self.SESSIONS[chat_id].messenger.send(
                update, f'{update.message.from_user.first_name} {e.args[0]}'
            )

    async def command_repeat(self, update: Update, context: CallbackContext):
        self.logger.info("Command repeat...")
        chat_id = update.message.chat_id
        if chat_id in self.SESSIONS:
            movie_img = self.SESSIONS[chat_id].quiz.get_question()
            await self.SESSIONS[chat_id].messenger.send_msg(
                chat_id, _("repeting")
            )
            await self.SESSIONS[chat_id].messenger.send_photo(
                chat_id=chat_id, photo=movie_img,
                caption=_("what_is_the_movie_series_name")
            )
            await self.SESSIONS[chat_id].messenger.send_msg(
                chat_id, "==========================="
            )
        else:
            await update.message.reply_text(_("session_not_found"))

    async def command_cut(self, update: Update, context: CallbackContext):
        self.logger.info("Command cut...")
        chat_id = update.message.chat_id
        if chat_id in self.SESSIONS:
            try:
                player = player.Player(update.message.from_user.id)
                self.SESSIONS[chat_id].player_quit(player)
                await self.SESSIONS[chat_id].messenger.send(
                    update, f'{player.name} {_("quit_the_game")}'
                )
            except ValueError as e:
                await self.SESSIONS[chat_id].messenger.send(
                    update, f'{update.message.from_user.first_name} {e.args[0]}'
                )
        else:
            await update.message.reply_text(_("session_not_found"))

    async def command_stop(self, update: Update, context: CallbackContext):
        self.logger.info("Command stop...")
        chat_id = update.message.chat_id
        if chat_id in self.SESSIONS:
            self.SESSIONS[chat_id].stop()
            await self.SESSIONS[chat_id].messenger.send(
                update, _("game_stopped")
            )
        else:
            await update.message.reply_text(_("session_not_found"))

    # Implement the command_check_resps method
    async def command_check_resps(self, update: Update, context: CallbackContext):
        self.logger.info("Checking responses...")
        chat_id = update.message.chat_id
        if chat_id in self.SESSIONS:
            user_response = update.message.text
            sess = self.SESSIONS[chat_id]
            # Add logic to handle user responses here
            await sess.messenger.send_msg(chat_id, f"Received: {user_response}")
        else:
            await update.message.reply_text(_("session_not_found"))


if __name__ == "__main__":
    Server()
