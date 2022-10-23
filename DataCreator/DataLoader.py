import sys
sys.path.insert(0,'..')

import DB
import Anekdotes

def f(text):
    return True

aneks = DB.get_all_aneks(sort=0)
print(len(aneks))

dataA = Anekdotes.make_data_for_model(aneks, 2 ,f)

DB.set_collection("Lentyach")
aneks = DB.get_all_aneks()
print(len(aneks))

dataL = Anekdotes.make_data_for_model(aneks,2,f)

DB.set_collection("Kalik")
aneks = DB.get_all_aneks()
print(len(aneks))

dataK = Anekdotes.make_data_for_model(aneks,2,f)

modelFull = Anekdotes.make_markov_model(dataA + dataL + dataK)

Anekdotes.generate_posts(model = modelFull, count= 10000, unique_check= True)
Anekdotes.generate_posts_donut(model = modelFull,count = 24 * 31 * 12 * 30, unique_check= True)

