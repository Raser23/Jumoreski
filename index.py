import config
import random
import telebot
import loadAneks

bot = telebot.TeleBot(config.TGtoken)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, random.choice(loadAneks.aneks))

if __name__ == '__main__':
    bot.polling(none_stop=True)