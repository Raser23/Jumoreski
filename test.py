
def f(text):
    return True
import DB
from markov.markov_model import make_markov_model
import Anekdotes

aneks = DB.get_all_aneks()

#print("aneks getted")
print(len(aneks))
data = Anekdotes.make_data_for_model([an for an in aneks if "шляп" in an],2,f)
print("Model ready")
DB.add_model("all_hat",data)

