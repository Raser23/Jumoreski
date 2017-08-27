
def f(text):
    return True

import DB
#l = DB.get_random_aneks(10)

from markov.markov_model import make_markov_model

#data = DB.get_model("test")
#print("data loaded")
#mdl = make_markov_model(data)
#print("Model builded")

#import Anekdotes
#aneks = DB.get_all_aneks()[:4500]
#print("aneks getted")
#data = Anekdotes.make_data_for_model(aneks,2,f)
#print("Model ready")
#DB.add_model("all_2",data)
#print("Model saved")


data = DB.get_model("all_2")
print(len(data))
