import vk
import config as CFG
import requests
import threading

session = vk.AuthSession(access_token=CFG.VKTOKEN)
api = vk.API(session)
data = api.groups.getLongPollServer(group_id=CFG.GROUPID, v=CFG.VKAPIVERSION)


def group_leave(update_obj):
    pass


def group_join(update_obj):
    pass


def message_new(update_obj):
    api.messages.send(user_id=update_obj['user_id'], peer_id=update_obj['user_id'], message="?", v=CFG.VKAPIVERSION)
    pass


handler = {"group_leave": group_leave,
           "group_join": group_join,
           "message_new": message_new}


def update_processing(update):
    print(update)
    update_type = update['type']
    update_obj = update['object']
    if update_type in handler:
        handler[update_type](update_obj)


def start_long_poll():
    t1 = threading.Thread(target=long_poll)
    t1.start()


def long_poll():
    while True:
        response = requests.get(
            '{server}?act=a_check&key={key}&ts={ts}&wait=25'.format(server=data['server'], key=data['key'], ts=data[
                'ts'])).json()
        updates = response['updates']

        if updates:  # проверка, были ли обновления
            for element in updates:  # проход по всем обновлениям в ответе
                update_processing(element)
        data['ts'] = response['ts']  # обновление номера последнего обновления
