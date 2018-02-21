
def f(text):
    return True
import DB
from markov.markov_model import make_markov_model
import Anekdotes





#aneks = DB.get_all_aneks()
aneks = DB.get_all_aneks()
print(len(aneks))
print("Aneks getted")

data = Anekdotes.make_data_for_model(aneks[:10040:2],2,f)
DB.add_model("all_1",data)
print("Model loaded")
data = Anekdotes.make_data_for_model(aneks[10040:],2,f)
DB.add_model("all_2",data)
print("Model loaded")

