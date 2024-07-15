#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import feedparser
import logging
import sqlite3
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from pathlib import Path

config = Path("./config.py")
try:
    config.resolve(strict=True)
except FileNotFoundError:
    print("Por favor, copia config.py.sample a config.py y rellena las propiedades.")
    exit()


import config

rss_dict = {}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# SQLITE
def sqlite_connect():
    global conn
    conn = sqlite3.connect('rss.db', check_same_thread=False)


def sqlite_load_all():
    sqlite_connect()
    c = conn.cursor()
    c.execute('SELECT * FROM rss')
    rows = c.fetchall()
    conn.close()
    return rows


def sqlite_write(name, link, last):
    sqlite_connect()
    c = conn.cursor()
    q = [(name), (link), (last)]
    c.execute('''INSERT INTO rss('name','link','last') VALUES(?,?,?)''', q)
    conn.commit()
    conn.close()


# RSS
def rss_load():
    # if the dict is not empty, empty it.
    if bool(rss_dict):
        rss_dict.clear()

    for row in sqlite_load_all():
        rss_dict[row[0]] = (row[1], row[2])


async def cmd_rss_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if bool(rss_dict) is False:
        await update.message.reply_text("The database is empty")
    else:
        for title, url_list in rss_dict.items():
            await update.message.reply_text(
                "Título: " + title +
                "\nURL RSS: " + url_list[0] +
                "\nÚltima noticia comprobada:" + url_list[1])


async def cmd_rss_add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # try if there are 2 arguments passed
    try:
        context.args[1]
    except IndexError:
        await update.message.reply_text("ERROR: EL formato debe ser: /add <título> <enlace>")
        raise
    # try if the url is a valid RSS feed
    try:
        rss_d = feedparser.parse(context.args[1])
        rss_d.entries[0]['title']
    except IndexError:
        await update.message.reply_text(
            "ERROR: EL enlace no parece ser un feed RSS o no es compatible")
        raise
    sqlite_write(context.args[0], context.args[1], str(rss_d.entries[0]['link']))
    rss_load()
    await update.message.reply_text("Añadido \nTÍTULO: %s\nRSS: %s" % (context.args[0], context.args[1]))
    print("Añadido \nTÍTULO: %s\nRSS: %s" % (context.args[0], context.args[1]))


async def cmd_rss_remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect('rss.db')
    c = conn.cursor()
    name = str(context.args[0])
    try:
        c.execute('DELETE FROM rss WHERE name = ?', [name])
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Error %s:' % e)
    rss_load()
    await update.message.reply_text("Borrado: " + name)
    print("Borrado: " + name)


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "RSS en Telegram bot" +
        "\n\nDespués de añadir con éxito un enlace RSS, el bot comienza a buscar la fuente cada "
        + str(config.delay) + " segundos. (Puedes configurarlo en config.py) ⏰⏰⏰" +
        "\n\nLos Títulos son usados para gestionar fácilmente los feeds RSS y deben contener solo una palabra 📝📝📝" +
        "\n\nComandos:" +
        "\n/help Muestra este mensaje de ayuda." +
        "\n/add <title> <link> Para añadir una RSS en la base de datos." +
        "\n/remove <title> Borra una RSS de la base de datos."
        "\n/list Listar todos los títulos y RSS guardados.")


async def rss_monitor(context: ContextTypes.DEFAULT_TYPE):
    for name, url_list in rss_dict.items():
        rss_d = feedparser.parse(url_list[0])
        if (url_list[1] != rss_d.entries[0]['link']):
            print("Nueva RSS para " + name + ", actualizando base de datos...")
            conn = sqlite3.connect('rss.db')
            q = [(str(rss_d.entries[0]['link'])), (name)]
            c = conn.cursor()
            c.execute('''UPDATE rss SET 'last' = ? WHERE name=? ''', q)
            conn.commit()
            conn.close()
            rss_load()
            print("Emviando RSS a Telegram...")
            await context.bot.send_message(config.chatid, rss_d.entries[0]['link'])
            print("Éxito.")


def init_sqlite():
    conn = sqlite3.connect('rss.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE rss (name text, link text, last text)''')


def main() -> None:
    dp = Application.builder().token(config.Token).build()

    dp.add_handler(CommandHandler("add", cmd_rss_add))
    dp.add_handler(CommandHandler("help", cmd_help))
    dp.add_handler(CommandHandler("start", cmd_help))
    dp.add_handler(CommandHandler("list", cmd_rss_list))
    dp.add_handler(CommandHandler("remove", cmd_rss_remove))

    #dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


    db = Path("./rss.db")
    try:
        db.resolve(strict=True)
    except FileNotFoundError:
        print("Base de datos no encontrada, intenta crear una nueva.")
        try:
            init_sqlite()
        except Exception as e:
            print("Error cuando se creaba la base de datos : ", e.message, e.args)
            pass
        else:
            print("Éxito.")

    rss_load()
    print("Corriendo RSS Monitor.")

    dp.job_queue.run_repeating(rss_monitor, config.delay)
    dp.run_polling(allowed_updates=Update.ALL_TYPES)
    conn.close()


if __name__ == '__main__':
    main()