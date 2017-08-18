import random
import loadAneks
import config
import telebot
import os
from flask import Flask, request

import testVK


bot = telebot.TeleBot(config.TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['anek'])
def send_anek(message):
    bot.send_message(message.chat.id, loadAneks.get_random())

@bot.message_handler(commands=['generate1'])
def generate(message):
    bot.send_message(message.chat.id, loadAneks.generate_anek1())

@bot.message_handler(commands=['generate2'])
def generate(message):
    bot.send_message(message.chat.id, loadAneks.generate_anek2())

@bot.message_handler(content_types=["text"])
def send_anek(message):
    bot.send_message(message.chat.id, random.choice(loadAneks.aneks))

@server.route("/bot", methods=['POST'])
def getMessage():
    s = request.stream.read().decode("utf-8")
    #print(s)
    updates = [telebot.types.Update.de_json(s)]
    message = updates[0].message
    chat = message.chat
    user = message.from_user
    print(message)
    print(chat)
    print(user)
    bot.send_message(chat.id, "SOsi pistrun")

    bot.process_new_updates(updates)
    return "ok", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.HOST +"/bot")
    return "!", 200

webhook()
server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)
