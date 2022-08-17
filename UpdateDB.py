import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping

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

#vk1.a.Y28peevw2gGNArRCv_twnj5GUezCsrVRRqmVSz0NMxDkOyrfqOJASvd4MmL1oHo4oPlbKI_C9T-mJNLXMHrtY26ytgWG0QhzLDzcHVEaeqiEnFc90l-d40XvWfR5U1mePQzyy0Ql1GlD-JqRAfzQ9bPhdfNgtKjfVh9HgxrN-RkL8YZGgl7hZU-mBgpwUzxn

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
