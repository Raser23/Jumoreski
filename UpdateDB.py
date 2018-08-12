import testVK

import DB




def UpdateH():
    DB.set_collection("anekdotes")
    testVK.UpdateAneks(DB.add_anek)

def LChecker(likesCount,text):
    return "#мудрость" in text

def UpdateL():
    DB.set_collection("Lentyach")
    testVK.UpdateAneks(DB.add_anek, domain= "lentyay_tv" , check_func = LChecker, load_all = True)
