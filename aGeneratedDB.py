from pymongo import MongoClient
import config as CFG
from os import listdir
from Things.StringHash import hash_string


current_collection = "Generated"

client = MongoClient(CFG.DBURL)

db = client[CFG.DBCLIENT]

def Add(text):
    resultObj = {"text" : text,
                 "hash" :hash_string(text)}
    db[current_collection].insert_one(resultObj)

def Count():
    return db[current_collection].count()

def Get():
    obj = db[current_collection].find_one()
    db[current_collection].delete_many(obj)
    return obj

