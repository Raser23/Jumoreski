import telebot
from flask import Flask, request
import config
import os
import random
bot = telebot.TeleBot(config.TOKEN)
server = Flask(__name__)

def debug(message):
    chat = message.chat
    user = message.from_user
    msg_text = message.text

    if int(chat.id) == int(config.DEBUGID):
        return

    debug_text = "*User*: "+str(user.first_name) +" "+ str(user.last_name)+"\n"
    #debug_text += "*Nickname*: "+str(user.username)+"\n"
    #debug_text += "*User ID*: " + str(user.id)+"\n"
    #debug_text += "*Message*: "+str(msg_text)+"\n"
    #debug_text += "*Chat ID*: "+str(chat.id)+"\n"
    #debug_text += "*Conversation type*: "+str(chat.type)
    send_debug(debug_text)

def send_debug(text):
    """"
    *bold text *
    _italic text_
    [text](URL)
    """
    #print(text)
    try:
        bot.send_message(config.DEBUGID,text,parse_mode="Markdown")
    except Exception as inst:
        print(inst)
        bot.send_message(config.DEBUGID, text)

import testVK
testVK.start(send_debug)
import loadAneks



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['anekdot'])
def send_anek(message):
    bot.send_message(message.chat.id, loadAneks.get_random())

@bot.message_handler(commands=['generate'])
def generate(message):
    bot.send_message(message.chat.id, loadAneks.generate_anek1())

@bot.message_handler(commands=['generate_short'])
def generate(message):
    bot.send_message(message.chat.id, loadAneks.generate_short())

@bot.message_handler(commands=['send_message'])
def send_anek(message):
    msg_text = message.text
    user_id = message.from_user.id
    conv_id = message.chat.id
    if(int(user_id) == int(config.OWNERID) and int(conv_id) == int(config.DEBUGID)):

        words = msg_text.split(" ")
        if (len(words) < 3):
            return

        send_msg = " ".join(words[2:])
        send_to_id = words[1]
        bot.send_message(send_to_id,send_msg)
    else:
        default_answer(message)

@bot.message_handler(commands=['info'])
def send_anek(message):
    debug(message)
    default_answer(message)

@bot.message_handler(content_types=["text"])
def default_answer(message):
    bot.send_message(message.chat.id, random.choice(loadAneks.aneks))





@server.route("/bot", methods=['POST'])
def get_message():
    s = request.stream.read().decode("utf-8")
    updates = [telebot.types.Update.de_json(s)]
    for update in updates:
        debug(update.message)

    bot.process_new_updates(updates)
    return "ok", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.HOST +"/bot")
    return "ok", 200

if(int(config.WH) == 1):
    print("Webhook setted")
    webhook()
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
    server = Flask(__name__)
else:
    print("Polling")
    bot.remove_webhook()
    bot.polling(none_stop = True)