import time
import threading
import config
import aGeneratedDB


from VKpost import post

def writer():
    while(True):

        if(config.VKPOSTING):
            post(aGeneratedDB.Get()["text"])
            print("posted")
        time.sleep(config.POSTCD)

    pass

if(config.VKPOSTING):
    t1 = threading.Thread(target=writer)
    t1.start()