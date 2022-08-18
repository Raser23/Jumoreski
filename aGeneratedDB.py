from Things.StringHash import hash_string
from Things.DBClient import getClient

current_collection = "Generated"

db = getClient()


def add(text):
    result_obj = {"text": text,
                  "hash": hash_string(text)}
    db[current_collection].insert_one(result_obj)


def add_donut(text):
    result_obj = {"text": text,
                  "hash": hash_string(text)}
    db["GeneratedDon"].insert_one(result_obj)



def count():
    return db[current_collection].count()


def get():
    obj = db[current_collection].find_one()
    db[current_collection].delete_many(obj)
    return obj

def getDonut():
    obj = db["GeneratedDon"].find_one()
    db["GeneratedDon"].delete_many(obj)
    return obj