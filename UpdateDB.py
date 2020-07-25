import testVK
import config as CFG
print(CFG.DBURL)
import DB


import Things.UpdateDBStuff as uds

def LoadHumserques():
    DB.set_collection(CFG.collections["hum"])
    testVK.UpdateAneks(DB.add_anek,
                       domain= CFG.domains["hum"],
                       check_func=uds.EmptyChecker(),
                       load_all = True)


def LoadLentyay():
    DB.set_collection(CFG.collections["lent"])
    testVK.UpdateAneks(DB.add_anek,
                       domain= CFG.domains["lent"] ,
                       check_func = uds.WordChecker(["#мудрость"]),
                       load_all = True)

def LoadKalik():
    DB.set_collection(CFG.collections["kal"])
    testVK.UpdateAneks(DB.add_anek,
                       domain= CFG.domains["kal"] ,
                       check_func = uds.EmptyChecker(),
                       load_all = True)

LoadHumserques()
LoadLentyay()
LoadKalik()
