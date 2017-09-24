import DB

aneks= DB.get_all_aneks_with_data()
print(len(aneks))

outputF = open("output.txt","w")
for anek in aneks:
    text = anek["text"] + " #END# "
    if("шляп" in text):
        outputF.write(text)