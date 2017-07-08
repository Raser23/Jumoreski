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
for i in onlyfiles:
    path = config.path+i
    f = open(path, 'r')
    text = prettify(f.read())
    aneks.append(text)

from random import choice

def get_random():
    return choice(aneks)


from markov.markov_model import make_markov_model


data = []
for i in aneks:
    if("шляпу" in i.split(" ")):
        data += ("#START# "+i+" #END#").split(" ")

model = make_markov_model(data)
from markov.sentence_generator import generate_random_sentence

def generate_anek():
    return generate_random_sentence(-1, model)

