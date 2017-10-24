def f(text):
    return True

import TextPrettifier as TP

import DB

DB.set_collection("testc")
import Anekdotes


aneks = DB.get_all_aneks()
print("Loaded "+str(len(aneks)) + " anekdotes")

for i in range(len(aneks)):
    if i % 1000 == 0:
        print(i)
    aneks[i] = TP.pret(aneks[i])


data = Anekdotes.make_data_for_model(aneks[:5500],2,f)
DB.add_model("test_1", data)
print("Model loaded")
data = Anekdotes.make_data_for_model(aneks[7000:],2,f)
DB.add_model("test_2", data)
print("Model loaded")
