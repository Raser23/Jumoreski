import telebot
from flask import Flask, request
import config
import os

import Predict as predicter

bot = telebot.TeleBot(config.TOKEN)
server = Flask(__name__)

import testVK as vk

import Bot.Debug as Debugger

Debugger.Start(bot.send_message)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['anekdot'])
def send_anek(message):
    bot.send_message(message.chat.id, Anekdotes.get_random())



@bot.message_handler(commands = ['predict'])
def pred(message):
    bot.reply_to(message,predicter.Answer(message));
    '''txt = message.text.split(" ")
    if(len(txt) == 1):
        bot.reply_to(message, 'После команды нужно ввести id пользователя ')
    else:


        userId = txt[1]
        if '/' in txt[1]:
            p = txt[1].split('/')
            userId = p[-1]

        result = predicter.PredictUser(userId)
        resultStr = ""
        if(result == 0):
            resultStr = "Говноед"
        else:
            resultStr = "Не говноед"
        bot.reply_to(message, resultStr)'''

@bot.message_handler(regexp="/generate")
def generate(message):
    bot.send_message(message.chat.id, Anekdotes.Answer(message))
    '''index = -1
    txt = message.text

    txt = txt.split(" ")
    msg =""
    index = txt[0][len("/generate"):]

    if("@" in index):
        index = index[:index.find('@')]

    if(index == "hat"):
        msg = Anekdotes.generate_hat_anek()
    elif(index == "short"):
        msg = Anekdotes.generate_short()
    elif(index == ""):
        index = 2
    else:
        index = int(index)
        if(index <1 or index>6):
            index = 2
        msg = Anekdotes.generate_anek(index)

    bot.send_message(message.chat.id,msg )'''


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
    Debugger.debug(message)
    default_answer(message)

@bot.message_handler(content_types=["text"])
def default_answer(message):
    bot.send_message(message.chat.id, Anekdotes.get_random())


#server handlers

@server.route("/bot", methods=['POST'])
def get_message():
    s = request.stream.read().decode("utf-8")
    updates = [telebot.types.Update.de_json(s)]
    #TODO: ебаный в рот
    for update in updates:
        #print(update.message)
        Debugger.debug(update.message)

    bot.process_new_updates(updates)
    return "ok", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.HOST +"/bot")
    return "ok", 200

@server.route("/wakeup")
def wakeup():
    #print("pinged")
    return "Never sleeps", 200

import testVK

testVK.start(Debugger.send_debug)

import Anekdotes
if(config.VKPOSTING):
    import VKposting
import NotSleeping
if(int(config.WH) == 1):
    print("Webhook setted")
    webhook()
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
    server = Flask(__name__)
else:
    print("Polling")
    bot.remove_webhook()
    bot.polling(none_stop = True)


