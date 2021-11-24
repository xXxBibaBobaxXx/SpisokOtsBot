import telebot
import config
import json
import traceback
from pip._internal.utils import logging

bot = telebot.TeleBot('2136203372:AAGFoXXLO6Md4hZbI_b83x5eOFUJ27NQ2Ng')
bot.polling(none_stop=True)
@bot.message_handler(commands=['/start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Hi')
    def help_message(arguments, message, CMD=None):
        response = {'chat_id': message['chat']['id']}
        result = ["Hey, %s!" % message["from"].get("first_name"),
                  "\rI can accept only these commands:"]
        for command in CMD:
            result.append(command)
        response['text'] = "\n\t".join(result)
        return response