import time
import threading
import config


def writer():
    while True:
        time.sleep(30*60)
        from VKBOT.Stats import add_report
        add_report()
        print("Report created")
        time.sleep(config.REPORTTIME)
    pass


t1 = threading.Thread(target=writer)
t1.start()
