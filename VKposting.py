import Anekdotes
import testVK
import time
import threading
import config
def writer():
    while(True):
        testVK.post_vk(Anekdotes.generate_anek(2))
        print("posted")
        time.sleep(config.POSTCD)
    pass

t1 = threading.Thread(target=writer)
t1.start()