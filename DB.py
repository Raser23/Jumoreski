import config
from os import listdir
from os.path import isfile, join

from Things.StringHash import hash_string
from Things.DBClient import getClient



current_collection = "anekdotes"

def set_collection(str):
    global current_collection
    current_collection = str
def reset_collection():
    global current_collection
    current_collection = "anekdotes"

db = getClient()
print("Connected to Database")
print(db.collection_names())
def prettify(str):
    while "<br>" in str:
        str = str.replace("<br>","\n")
    return  str

def form_anek(post):
    if("likes" not in post):
        return {"text": post, "hash": hash_string(post), "likes": 0}

    likesCount = post["likes"]["count"]
    text = prettify(post["text"])
    return {"text":text,"hash":hash_string(text),"likes":likesCount}


def get_random_anek():
    return list(db[current_collection].aggregate([{"$sample": {"size": 1}}]))[0]["text"]
def get_random_anek_with_data():
    return list(db[current_collection].aggregate([{"$sample": {"size": 1}}]))[0]

def sortByLength(inputStr):
    return inputStr["likes"]

def get_all_aneks(sort = 0):
    print("Goind to load all aneks (sort = "+str(sort)+")...")
    b = list(get_all_aneks_with_data())
    print("Aneks getted...")
    if(sort == 1):
        b.sort(key=sortByLength,reverse=True)
    return [a["text"] for a in b]


def get_all_aneks_with_data():
    b = db[current_collection].find()
    return [a for a in b]

def get_random_aneks(count):
    return  [a["text"] for a in list(db[current_collection].aggregate([{"$sample": {"size": count}}]))]

anekdotes = []

def add_anek(post):
    anek = form_anek(post)
    if (db[current_collection].find_one({"hash": anek["hash"]}) != None):
        return
    str(db[current_collection].insert_one(anek))

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

def is_unique(hash):
    return db["anekdotes"].find_one({"hash" : hash}) is None
