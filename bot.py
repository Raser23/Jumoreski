import telebot
from flask import Flask, request
import config
import os
import random
bot = telebot.TeleBot(config.TOKEN)
server = Flask(__name__)
import testVK as vk
def debug(message):

    chat = message.chat
    user = message.from_user
    msg_text = message.text

    if int(chat.id) == int(config.DEBUGID):
        return

    debug_text = "*User*: "+str(user.first_name) +" "+ str(user.last_name)+"\n"
    debug_text += "*Nickname*: "+str(user.username)+"\n"
    debug_text += "*User ID*: " + str(user.id)+"\n"
    debug_text += "*Message*: "+str(msg_text)+"\n"
    debug_text += "*Chat ID*: "+str(chat.id)+"\n"
    debug_text += "*Conversation type*: "+str(chat.type)
    send_debug(debug_text)

def send_debug(text):
    def edit_msg_text(txt):
        chars = ["*", "_", "[", "]", "(", ")", "\""]
        for ch in chars:
            while ch in txt:
                txt = txt.replace(ch," ")
        return txt
    """"
    *bold text *
    _italic text_
    [text](URL)
    """
    #print(text)
    try:
        bot.send_message(config.DEBUGID,text,disable_notification = True,parse_mode="Markdown")
        pass
    except Exception as inst:
        print(inst)
        bot.send_message(config.DEBUGID,text,disable_notification = True)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['anekdot'])
def send_anek(message):
    bot.send_message(message.chat.id, Anekdotes.get_random())

@bot.message_handler(commands=['generateshort'])
def generate(message):
    bot.send_message(message.chat.id, Anekdotes.generate_short())


@bot.message_handler(regexp="/generate")
def generate(message):
    index = -1
    txt = message.text

    txt = txt.split(" ")
    index = txt[0][len("/generate"):]
    if(index == "hat"):
        bot.send_message(message.chat.id, Anekdotes.generate_hat_anek())
        return

    if(index == ""):
        index = 2
    else:
        index = int(index)
    if(index <1 or index>6):
        index = 2

    txt = Anekdotes.generate_anek(index)
    vk.post_vk(txt)
    bot.send_message(message.chat.id,txt )


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

@bot.message_handler(commands=['i_nfo'])
def send_anek(message):
    debug(message)
    default_answer(message)

@bot.message_handler(content_types=["text"])
def default_answer(message):
    bot.send_message(message.chat.id, Anekdotes.get_random())



#dvach

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

import testVK
testVK.start(send_debug)
import Anekdotes

if(int(config.WH) == 1):
    print("Webhook setted")
    webhook()
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
    server = Flask(__name__)
else:
    print("Polling")
    bot.remove_webhook()
    bot.polling(none_stop = True)


