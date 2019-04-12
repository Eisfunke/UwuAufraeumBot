#!/usr/bin/python3

# benötigt python-telegram-bot

from telegram.ext import Updater, RegexHandler
import time

TOKEN_FILE = "token"

def delete(bot, update):
    time.sleep(2)
    bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)
    bot.sendMessage(chat_id=update.message.chat.id, text='An illegal uwu by ' + update.message.from_user.name + ' has been deleted here.')


token = open(TOKEN_FILE, "r").read().rstrip()
updater = Updater(token=token)

updater.dispatcher.add_handler(RegexHandler('.*\\b[uU]\s*([wWω]|[vV]\s*[vV])\s*[uU]\\b.*', delete))

updater.start_polling()
