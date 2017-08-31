
def f(text):
    return True
import DB
from markov.markov_model import make_markov_model
import Anekdotes

aneks = DB.get_all_aneks()

#print("aneks getted")
print(len(aneks))
data = Anekdotes.make_data_for_model(aneks[:5000],2,f)
print("Model ready")
DB.add_model("all_b_1",data)
data = Anekdotes.make_data_for_model(aneks[5000:10000],2,f)
print("Model ready")
DB.add_model("all_b_2",data)
data = Anekdotes.make_data_for_model(aneks[10000:],2,f)
print("Model ready")
DB.add_model("all_b_3",data)
