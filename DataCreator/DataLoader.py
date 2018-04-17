
def f(text):
    return True
import DB
from markov.markov_model import make_markov_model
import Anekdotes

print("here");



#aneks = DB.get_all_aneks()
aneks = DB.get_all_aneks()
print(len(aneks))
print("Aneks getted")

data = Anekdotes.make_data_for_model(aneks[5020:10040:2],1,f)
DB.add_model("all_1",data)
print("Model loaded")
data = Anekdotes.make_data_for_model(aneks[10040:14000:2],2,f)
data = Anekdotes.make_data_for_model(aneks[14000:],2,f)
DB.add_model("all_2",data)
print("Model loaded")

