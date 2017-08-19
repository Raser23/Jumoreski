import config
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
from random import choice
from markov.markov_model import make_markov_model
def prettify(str):
    while "<br>" in str:
        str = str.replace("<br>","\n")
    return  str
aneks = []

def make_model(path,count,func):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for text in onlyfiles:
        file_path = path + text
        f = open(file_path, 'r')
        text = prettify(f.read())
        aneks.append(text)

    data = []
    for text in aneks:

        if(not func(text)):
            continue

        anek_data = []
        words = text.split(" ")

        for k in range(count):
            anek_data.append("#START#")
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
    return make_markov_model(data)

def get_random():
    return choice(aneks)


counter = 0
def f(text):
    return True
def f1(text):
    global counter
    counter +=1
    return counter == 3

#tst_model = make_model("test/",5,f)
#TODO: сделать нормальное начало анеков

models = {}

for i in range(1,5):
    models.setdefault(i,[])
    models[i] = make_model(config.path,i,f)
    print("Model number {} ready".format(i))

def f2(text):
    return "шляп" in text

hat_model = make_model(config.path,2,f2)
print("hat model ready")

from markov.sentence_generator import generate_random_sentence

def generate_anek(model_index):
    return generate_random_sentence(-1, models[model_index],max_words = (360*2)/model_index)

def generate_hat_anek():
    return generate_random_sentence(-1, hat_model,max_words = 100)

def generate_short(model_index):
    return generate_random_sentence(-1, models[2],max_words=10)


