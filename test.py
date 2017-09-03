
def f(text):
    return True
import DB
from markov.markov_model import make_markov_model
import Anekdotes





#aneks = DB.get_all_aneks()
aneks = []
data = Anekdotes.make_data_for_model(aneks,2,f)
mdl = Anekdotes.make_markov_model(data)
print(Anekdotes.generate(mdl))