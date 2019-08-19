import config as CFG
import vk


def post(text):
    session = vk.AuthSession(access_token=CFG.VKAPIUSER)
    vk_api = vk.API(session)
    vk_api.wall.post(v = 5.73,owner_id= -152671561,
                      from_group= 1,
                      message= text,
                      signed = 1
                     )