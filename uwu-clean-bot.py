#!/usr/bin/python3

# benötigt python-telegram-bot

from telegram.ext import Updater, RegexHandler
import time

TOKEN_FILE = "token"

def delete(bot, update):
    time.sleep(10)
    bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)
    bot.sendMessage(chat_id=update.message.chat.id, text='A illegal uwu has been deleted here.')


token = open(TOKEN_FILE, "r").read().rstrip()
updater = Updater(token=token)

updater.dispatcher.add_handler(RegexHandler('.*\\b[uU][wW][uU]\\b.*', delete))

updater.start_polling()
