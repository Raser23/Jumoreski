
def f(text):
    return True
import DB
import Anekdotes

print("here")



#aneks = DB.get_all_aneks()
aneks = DB.get_all_aneks(sort=0)
print(len(aneks))
#print("Aneks getted")

data = Anekdotes.make_data_for_model(aneks[10000:15000:2], 2 ,f)
DB.add_model("all_1",data)
print("Model loaded")
#data = Anekdotes.make_data_for_model(aneks[10040:14000:2],2,f)
data = Anekdotes.make_data_for_model(aneks[17000::1],2,f)
DB.add_model("all_2",data)

DB.set_collection("Lentyach")
aneks = DB.get_all_aneks()
data = Anekdotes.make_data_for_model(aneks,2,f)
DB.add_model("all_3",data)

print("Model loaded")

