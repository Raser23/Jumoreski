import time
import threading
import config

import urllib3
http = urllib3.PoolManager()
def writer():
    while(True):
        print("pinging")
        r = http.request('GET', config.HOST +"/wakeup")
        print(r.status)
        time.sleep(config.POSTCD)
    pass

t1 = threading.Thread(target=writer)
t1.start()