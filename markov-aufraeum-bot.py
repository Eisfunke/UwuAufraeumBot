#!/usr/bin/python3

# benötigt python-telegram-bot

from telegram.ext import Updater, RegexHandler
import time

TOKEN_FILE = "token"

def delete(bot, update):
    time.sleep(10)
    bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)


token = open(TOKEN_FILE, "r").read().rstrip()
updater = Updater(token=token)

updater.dispatcher.add_handler(RegexHandler('uwu|UWU|uWu|UwU|Uwu|uwU', delete))

updater.start_polling()
