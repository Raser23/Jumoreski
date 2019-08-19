import time
import threading
import config


def writer():
    while True:
        from VKBOT.Stats import add_report
        add_report()
        time.sleep(config.REPORTTIME)

    pass


t1 = threading.Thread(target=writer)
t1.start()
