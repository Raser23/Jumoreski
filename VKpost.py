import config as CFG
import vk
import telebot

def post(text):

    tok = CFG.VKB
    session = vk.AuthSession(access_token=tok)
    vk_api = vk.API(session)

    vk_api.wall.post(v = CFG.VKAPIVERSION,owner_id= "-"+CFG.GROUPID,
                      from_group= 1,
                      message= text,
                      signed = 1
                     )

    bot = telebot.TeleBot(CFG.TOKEN)
    bot.send_message("@neuraljumoresques", text)

def postDonut(text):
    tok = CFG.VKF
    session = vk.AuthSession(access_token=tok)
    vk_api = vk.API(session)

    vk_api.wall.post(v=CFG.VKAPIVERSION, owner_id="-"+CFG.GROUPID,
                     from_group = 1,
                     message = text,
                     signed = 1,
                     donut_paid_duration = -1
                     )