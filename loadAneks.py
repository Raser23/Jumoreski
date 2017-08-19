import config
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

def prettify(str):
    while "<br>" in str:
        str = str.replace("<br>","\n")
    return  str

aneks = []
onlyfiles = [f for f in listdir(config.path) if isfile(join(config.path, f))]
for text in onlyfiles:
    path = config.path + text
    f = open(path, 'r')
    text = prettify(f.read())
    aneks.append(text)

from random import choice

def get_random():
    return choice(aneks)


from markov.markov_model import make_markov_model


data = []
for text in aneks:
    #if("шляпу" in text.split(" ")):
    anek_data = []
    words = text.split(" ")
    anek_data.append("#START#")
    for i in range(0,len(words)-1,2):
        anek_data.append(words[i] +" "+ words[i+1])
    anek_data.append("#END#")
    anek_data.append("#START#")

    for i in range(1,len(words)-1,2):
        anek_data.append(words[i] +" "+ words[i+1])
    anek_data.append("#END#")

    data += anek_data

#print(data)
model1 = make_markov_model(data)
data = []
for text in aneks:
    if("шляпу" not in text.split(" ")):
        continue

    data += (["#START#"] + text.split(" ") + ["#END#"])

model2 = make_markov_model(data)


from markov.sentence_generator import generate_random_sentence

def generate_anek1():
    return generate_random_sentence(-1, model1)

def generate_short():
    return generate_random_sentence(-1, model1,max_words=20)


