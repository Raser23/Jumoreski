from pymongo import MongoClient
import config as CFG

def getClient():
    client = MongoClient(CFG.DBURL,retryWrites = False)
    return client[CFG.DBCLIENT]