import time
import threading
import config
import aGeneratedDB


from VKpost import post, postDonut

def writer():
    while(True):

        if(config.VKPOSTING):
            try:
                post(aGeneratedDB.get()["text"])
                print("posted")
            except BaseException as err:
                print("post failed")
                print(err)
            try:
                postDonut(aGeneratedDB.getDonut()["text"])
                print("posted donut")
            except:
                print("donut failed")
        time.sleep(config.POSTCD)

    pass

if(config.VKPOSTING):
    t1 = threading.Thread(target=writer)
    t1.start()
