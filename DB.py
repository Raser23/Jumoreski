from pymongo import MongoClient
import config
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
from random import choice
import hashlib
#dvach
client = MongoClient("mongodb://DB:qwerty12345@ds159953.mlab.com:59953/heroku_5dqf5tjw")
db = client["heroku_5dqf5tjw"]
print("Connected to Database")

def prettify(str):
    while "<br>" in str:
        str = str.replace("<br>","\n")
    return  str

def hash_string(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()

def form_anek(text):
    text = prettify(text)
    return {"text":text,"hash":hash_string(text)}


def get_random_anek():
    return  list(db.aneks.aggregate([{"$sample": {"size": 1}}]))[0]["text"]

def get_all_aneks():
    return [a["text"] for a in db.aneks.find()]

def get_random_aneks(count):
    return  [a["text"] for a in list(db.aneks.aggregate([{"$sample": {"size": count}}]))]

aneks = []

def add_anek(text):
    #print("adding")
    anek = form_anek(text)
    if (db.aneks.find_one({"hash": anek["hash"]}) != None):
        # print("anek already in db")
        return
    db.aneks.insert_one(anek)

def add_model(model_name,data):
    if (db.models.find_one({"name": model_name}) != None):
        db.models.find_one_and_update({"name": model_name},{'$set': {'data': data}})
    else:
        db.models.insert_one({"name":model_name,"data":data})

def get_model(name):
    return db.models.find_one({"name":name})["data"]


def load_aneks_to_db(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        try:
            file_path = path + file
            f = open(file_path, 'r',encoding='utf-8')
            add_anek(f.read())
        except Exception as e:
            print(e)
            pass
