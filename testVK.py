import vk
import config





def prettify(str):
    while "  " in str:
        str.replace("  "," ")
    if(str[0] == " "):
        str = str[1:]
    if(str[-1] == " "):
        str = str[:-1]
    return  str


def func(a):
    print("hui")

bot_debugger = func

def UpdateAneks():
    import testVkConfig as VKconfig
    print("Start updating...")
    session = vk.AuthSession(access_token = config.VKTOKEN)
    vk_api = vk.API(session)
    f = open("downloadedc", 'r')

    downloaded_count = int( f.read())
    print("Downloaded: "+str(downloaded_count))
    posts = vk_api.wall.get(domain=config.domain, offset=0)
    current_count = posts[0]
    count = 0
    need_to_download = current_count - downloaded_count
    debug_text=("*downloaded:* " + str(downloaded_count)) + "\n"
    debug_text+=("*current:* " + str(current_count)) + "\n"
    debug_text+=("*need to download:* " + str(need_to_download)) + "\n"
    while (True):
        try:
            current_posts = vk_api.wall.get(domain=config.domain, offset=count)[1:]
            for post in current_posts:
                if (count >= need_to_download):
                    break
                if(count % 10 == 0):
                    print("counter: " + str(count))
                name = str(current_count - count-1)
                text = post['text']

                if(text != ""):
                    f = open(config.path+name, 'w')
                    f.write(text)

                count += 1
            if (count >= need_to_download):
                break
        except Exception as e:
            print(e)
            continue
    tvkc = open("downloadedc", "w")
    s = "{}".format(str(current_count))
    debug_text+="new downloaded count: "+s+"\n"
    print("New downloaded count: "+str(s))
    try:
        tvkc.write(s)
        debug_text += "config saved"
    except Exception as e:
        print(e)
    bot_debugger(debug_text)


import threading,time

def Updater():
    UpdateAneks()


def set_updater():
    print("Updater setted...")
    Updater()


def start(debug):
    global bot_debugger
    bot_debugger = debug
    set_updater()





