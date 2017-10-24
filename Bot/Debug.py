import config as CFG


def func(a):
    print("hui")

send_message = func

def debug(message):

    chat = message.chat
    user = message.from_user
    msg_text = message.text
    if int(chat.id) == int(CFG.DEBUGID):
        return
    debug_text = "*User*: "+str(user.first_name) +" "+ str(user.last_name)+"\n"
    debug_text += "*Nickname*: "+str(user.username)+"\n"
    debug_text += "*User ID*: " + str(user.id)+"\n"
    debug_text += "*Message*: "+str(msg_text)+"\n"
    debug_text += "*Chat ID*: "+str(chat.id)+"\n"
    debug_text += "*Conversation type*: "+str(chat.type)
    send_debug(debug_text,send_message)

def send_debug(text):
    def edit_msg_text(txt):
        chars = ["*", "_", "[", "]", "(", ")", "\""]
        for ch in chars:
            while ch in txt:
                txt = txt.replace(ch," ")
        return txt
    """"
    *bold text *
    _italic text_
    [text](URL)
    """
    try:
        send_message(CFG.DEBUGID,text,disable_notification = True,parse_mode="Markdown")
        pass
    except Exception as inst:
        print(inst)
        send_message(CFG.DEBUGID,text,disable_notification = True)

def Start(sm):
    global send_message
    send_message = sm