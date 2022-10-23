import config as CFG
import telebot

bot = telebot.TeleBot("360853899:AAFH5OLI-l5fHXovtb2eH48jGNaIKBh90JM")
print(bot.get_me())
bot.send_message("@neuraljumoresques", "Всем привет")