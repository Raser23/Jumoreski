from pymongo import MongoClient
import config as CFG

def getClient():
    client = MongoClient(CFG.DBURL)
    #print(client['__my_database__'])
    print(client['test']['anekdotes'].find_one())
    return client['test']