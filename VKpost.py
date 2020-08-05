import config as CFG
import vk
from random import choice

def post(text):

    tok = choice([CFG.VKB,CFG.VKF])
    session = vk.AuthSession(access_token=tok)
    vk_api = vk.API(session)

    vk_api.wall.post(v = 5.122,owner_id= -152671561,
                      from_group= 1,
                      message= text,
                      signed = 1
                     )