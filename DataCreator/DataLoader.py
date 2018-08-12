
def f(text):
    return True
import DB
from markov.markov_model import make_markov_model
import Anekdotes

print("here")



#aneks = DB.get_all_aneks()
aneks = DB.get_all_aneks(sort=1)
print(len(aneks))
#print("Aneks getted")

data = Anekdotes.make_data_for_model(aneks[0:2510:2],1,f)
DB.add_model("all_1",data)
print("Model loaded")
#data = Anekdotes.make_data_for_model(aneks[10040:14000:2],2,f)
data = Anekdotes.make_data_for_model(aneks[2510:4700:2],1,f)
DB.add_model("all_2",data)

DB.set_collection("Lentyach")
aneks = DB.get_all_aneks()
data = Anekdotes.make_data_for_model(aneks,1,f)
DB.add_model("all_3",data)

print("Model loaded")

