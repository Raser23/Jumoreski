import config
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
from random import choice
from markov.markov_model import make_markov_model
from tqdm import tqdm
def prettify(str):
    while "<br>" in str:
        str = str.replace("<br>","\n")
    return  str

def make_data_for_model(aneks, count, func):

    data = []
    for text in aneks:

        if(not func(text)):
            continue

        anek_data = []
        words = text.split(" ")

        for k in range(count):
            #anek_data.append("#START#")
            start_s = " ".join(words[:k])
            if(start_s !="" and start_s!=" "):
                anek_data.append(start_s)

            j =-1
            for i in range(k, len(words) - count + 1, count):
                s=""
                for j in range(count):
                    s+= words[i+j]+" "
                s=s[:-1]
                anek_data.append(s)
                j=i

            last_s = " ".join(words[j+count:])
            if(last_s!=" " and last_s!=""):
                anek_data.append(last_s)

            anek_data.append("#END#")


        data += anek_data
    #print(data)
    return data

def make_model(aneks,count,func):
    return make_markov_model(make_data_for_model(aneks,count,func))


import DB
def get_random():
    return DB.get_random_anek()

#loading data
mdl = make_markov_model(DB.get_model("all_1")+DB.get_model("all_2") + DB.get_model("all_3"))

from markov.sentence_generator import generate_random_sentence

def generate_anek():

    return generate_random_sentence( mdl,fixedLength = -1, max_words = (35),rand=-1)

def generate_hat_anek():
    return "Данная опция пока не доступна ... "#generate_random_sentence(-1, hat_model,max_words = 100)

def generate_short():
    return generate_random_sentence(-1, mdl,max_words=10,rand=1)

def generate(model):
    return generate_random_sentence(-1, model,max_words = (360*2))


def Answer(message):
    index = -1
    txt = message.text

    txt = txt.split(" ")
    msg = ""
    index = txt[0][len("/generate"):]

    if ("@" in index):
        index = index[:index.find('@')]

    if (index == "hat"):
        msg = generate_hat_anek()
    elif (index == "short"):
        msg = generate_short()
    elif (index == ""):
        index = 2
    else:
        index = int(index)
        if (index < 1 or index > 6):
            index = 2
        msg = generate_anek(index)

    return msg

def generate_post():
    text = ""
    text += generate_anek()
    return text

def generate_posts(count = 100):
    from aGeneratedDB import Add

    for i in tqdm(range(count)):
        Add(generate_anek())
