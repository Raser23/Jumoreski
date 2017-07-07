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

