import vk
import config
import testVkConfig as VKconfig

from bot import send_debug as bot_debugger

def prettify(str):
    while "  " in str:
        str.replace("  "," ")
    if(str[0] == " "):
        str = str[1:]
    if(str[-1] == " "):
        str = str[:-1]
    return  str

def UpdateAneks():
    session = vk.AuthSession(access_token = config.VKTOKEN)
    vk_api = vk.API(session)
    downloaded_count = VKconfig.downloaded
    posts = vk_api.wall.get(domain=config.domain, offset=0)
    current_count = posts[0]
    count = 0
    need_to_download = current_count - downloaded_count


    debug_text=("*downloaded:* " + str(downloaded_count)) +"\n"
    debug_text+=("*current:* " + str(current_count))+"\n"
    debug_text+=("*need to download:* " + str(need_to_download))
    print(debug_text)
    bot_debugger(debug_text)

    while (True):
        try:
            current_posts = vk_api.wall.get(domain=config.domain, offset=count)[1:]
            for post in current_posts:
                if (count >= need_to_download):
                    break

                name = str(current_count - count-1)
                text = post['text']
                if(text != ""):
                    f = open(config.path+name, 'w')
                    f.write(text)
                count += 1
            if (count >= need_to_download):
                break
        except:
            # To many requests
            continue
    tvkc = open("testVKConfig.py", "w")
    s = "downloaded = {}".format(str(current_count))
    try:
        tvkc.write(s)
    except:
        print("err...")

import threading,time

def Updater():
    while 1488 == 32 * 46.5:
        print("start updating...")
        UpdateAneks()
        time.sleep(config.UPDATETIME)

t = threading.Thread(target=Updater)
t.start()






