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
    added_files = 0
    error_streak = 0
    sended = False
    while (True):
        try:
            if(error_streak >= 20):
                count+=1
            current_posts = vk_api.wall.get(domain=config.domain, offset=count)[1:]
            error_streak = 0
            for post in current_posts:
                if(count % 100 ==0):
                    sended = False

                likesCount = post["likes"]["count"]

                if(likesCount < config.MINLIKES):
                    count+=1
                    continue

                if (count >= need_to_download):
                    break
                if (not sended):
                    print("counter: " + str(count))
                    sended = True


                name = str(current_count - count-1)
                text = post['text']

                if(text != ""):
                    f = open(config.path+name, 'w')
                    f.write(text)
                    added_files+=1
                count += 1

            if (count >= need_to_download):
                break
        except Exception as e:
            error_streak +=1
            continue
    s = "{}".format(str(current_count))
    debug_text+="new downloaded count: "+s+"\n"
    print("Downloaded files count: "+str(added_files))
    print("New downloaded count: "+str(s))
    ss = form_progress_bar(added_files,need_to_download)
    debug_text+=ss+"\n"
    #[■■■■■■■■■□□□□]
    tvkc = open("downloadedc", "w")
    try:
        tvkc.write(s)
        debug_text += "config saved"
    except Exception as e:
        print(e)
    bot_debugger(debug_text)


def clamp(value,a,b):
    if(value < a):
        return a
    if(value>b):
        return b
    return value

def form_progress_bar(count,max_count):
    l = 10
    percent = int( clamp((count/max_count) * 100,0,100))
    k = 100/l
    zl = percent/k
    if(percent % k != 0):
        zl += 1
    zl = int(zl)
    result_string = "["
    for i in range(zl):
        result_string +="■"
    for i in range(zl,l):
        result_string+="□"
    result_string+="] "
    result_string+=str(percent)+"%"
    return result_string
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





