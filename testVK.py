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
    print(downloaded_count)
    posts = vk_api.wall.get(domain=config.domain, offset=0)
    current_count = posts[0]
    count = 0
    need_to_download = current_count - downloaded_count
    debug_text=("*downloaded:* " + str(downloaded_count)) +"\n"
    debug_text+=("*current:* " + str(current_count))+"\n"
    debug_text+=("*need to download:* " + str(need_to_download)) +"\n"
    #print(debug_text)

    while (True):
        try:
            current_posts = vk_api.wall.get(domain=config.domain, offset=count)[1:]
            for post in current_posts:

                if (count >= need_to_download):
                    break
                b = count%300 == 0 or count == need_to_download -1
                if b:
                    debug_text += str(count) + "..."

                name = str(current_count - count-1)
                text = post['text']
                if(text != ""):
                    f = open(config.path+name, 'w')
                    f.write(text)
                    if(b):
                        debug_text+="downloaded and saved"+"\n"
                else:
                    if(b):
                        debug_text += "is empty" + "\n"
                count += 1
            if (count >= need_to_download):
                break
        except Exception as e:
            # To many requests
            print(e)
            print(count)
            continue
    tvkc = open("downloadedc", "w")
    s = "{}".format(str(current_count))
    try:
        tvkc.write(s)
        debug_text += "config saved"
    except Exception as e:
        print(e)
    bot_debugger(debug_text)


import threading,time

def Updater():
    while True:
        UpdateAneks()
        time.sleep(config.UPDATETIME)


def set_updater():
    print("Updater setted...")
    t = threading.Thread(target=Updater)
    t.start()


def start(debug):
    set_updater()
    global bot_debugger
    bot_debugger = debug




