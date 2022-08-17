import time
import threading
import config
import aGeneratedDB


from VKpost import post, postDonut

def writer():
    while(True):

        if(config.VKPOSTING):
            post(aGeneratedDB.get()["text"])
            print("posted")
            postDonut(aGeneratedDB.getDonut()["text"])
            print("posted donut")
        time.sleep(config.POSTCD)

    pass

if(config.VKPOSTING):
    t1 = threading.Thread(target=writer)
    t1.start()