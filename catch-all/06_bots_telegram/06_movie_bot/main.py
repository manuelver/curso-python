from telegram.ext import CommandHandler, MessageHandler, filters, CallbackQueryHandler

from src import Botz


def main():

    print(r"""
    
                                      _                
     _ __ ___   __ _ _ __  _   _  ___| |_   _____ _ __ 
    | '_ ` _ \ / _` | '_ \| | | |/ _ \ \ \ / / _ \ '__|
    | | | | | | (_| | | | | |_| |  __/ |\ V /  __/ |   
    |_| |_| |_|\__,_|_| |_|\__,_|\___|_| \_/ \___|_|   """)

    bot = Botz()

    bot.app.add_handler(CommandHandler('start', bot.start_command))

    bot.app.add_handler(CommandHandler('help', bot.help_command))

    bot.app.add_handler(CommandHandler("find", bot.find_title))

    bot.app.add_handler(CommandHandler("save", bot.movie_saver))

    bot.app.add_handler(CommandHandler("remove", bot.movie_remover))

    bot.app.add_handler(CommandHandler("list", bot.movie_list))

    bot.app.add_handler(CommandHandler("reboot", bot.reboot))

    bot.app.add_handler(CommandHandler("status", bot.status))

    bot.app.add_handler(MessageHandler(filters.TEXT, bot.any_text))

    bot.app.add_error_handler(bot.error)

    bot.app.add_handler(CallbackQueryHandler(bot.query_handler))

    print('Bot Started Polling! Check Terminal for Errors')

    bot.app.run_polling(poll_interval=3)


if __name__ == '__main__':
    main()
