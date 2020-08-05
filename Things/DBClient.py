from pymongo import MongoClient
import config as CFG

def getClient():
    client = MongoClient(CFG.DBURL)
    return client['test']