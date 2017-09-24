import re
def f(text):
    return True
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def pret(text):
    re1 = re.compile("[^0-9,а-я,А-Я,A-Z,a-z, ,.,!,-,—,ё,Ё,-,?,-,\n]")
    text = re.sub(re1, " ", text)




    while "  " in text:
        text = text.replace("  "," ")

    text = text.replace("\n ", "\n")

    while " ." in text:
        text = text.replace(" .",".")

    end_of_s = [".","!","?","\n"]
    for ch in end_of_s:
        while ch +" " in text:
            text = text.replace(ch +" ",ch)

    while "\n\n" in text:
        text = text.replace("\n\n","\n")

    endof_sent = re.compile("[.!?]")

    indexes = []
    for ch in end_of_s:
        indexes = indexes + list(find_all(text,ch))

    indexes.sort()
    #print(indexes)
    prev_ind = 0
    sent = []
    for ind in indexes:
        sent.append(text[prev_ind:ind+1])
        prev_ind = ind +1


    #print(sent)

    not_empty_sent = []
    for i in range(len(sent)):
        if(len(sent[i]) > 0):
            not_empty_sent.append(sent[i][0].upper()+sent[i][1:].lower())

    #print(not_empty_sent)
    text = "".join(not_empty_sent)
    text = text.replace(".",". ")
    return text

import DB

DB.set_collection("testc")
import Anekdotes


aneks = DB.get_all_aneks()
print("Aneks getted")
data = Anekdotes.make_data_for_model(aneks[:5500],2,f)
DB.add_model("test_1",data)
print("Model loaded")
data = Anekdotes.make_data_for_model(aneks[5500:],2,f)
DB.add_model("test_2",data)
print("Model loaded")
