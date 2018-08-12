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
    print("Debug function")

def LikeChecker(likesCount, text):
    return likesCount >= config.MINLIKES


bot_debugger = func

def UpdateAneks(save_func ,domain = config.domain,check_func = LikeChecker , load_all = False):
    #import testVkConfig as VKconfig
    print("Start updating...")
    session = vk.AuthSession(access_token = config.VKTOKEN)
    vk_api = vk.API(session)
    f = open("downloadedc", 'r')

    downloaded_count = 0 if load_all else int(f.read())

    #print("Downloaded: "+str(downloaded_count))
    posts = vk_api.wall.get(domain=domain, offset=0,v=5.73)

    print(posts)
    current_count = posts['count']
    count = 0
    need_to_download = current_count - downloaded_count
    debug_text=("*downloaded:* " + str(downloaded_count)) + "\n"
    debug_text+=("*current:* " + str(current_count)) + "\n"
    debug_text+=("*need to download:* " + str(need_to_download)) + "\n"
    print(debug_text)
    added_files = 0
    error_streak = 0
    sended = False
    while (True):
        try:
            if(error_streak >= 20):
                count+=1
            current_posts = vk_api.wall.get(domain=domain, offset=count,v=5.73)['items']
            error_streak = 0
            for post in current_posts:
                if(count % 100 ==0):
                    sended = False

                likesCount = post["likes"]["count"]
                text = post['text']

                # Переход к следующему анекдоту
                if not check_func(likesCount,text):
                    count+=1
                    continue

                # Видимо мы скачали все что хотели
                if (count >= need_to_download):
                    break
                # Штука для дебага
                if (not sended):
                    print("counter: " + str(count))
                    sended = True



                if(text != ""):
                    save_func(post)
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
    if(max_count == 0):
        return  form_progress_bar(100,100)
    l = 10
    percent = int( clamp( (count/max_count) * 100,0,100))
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
    #set_updater()


def post_vk(text):
    session = vk.AuthSession(access_token=config.VKTOKEN)
    vk_api = vk.API(session)
    vk_api.wall.post(owner_id= -152671561,
                      from_group= 1,
                      message= text,
                      version = 5.73
                     )



#post_vk()