from Funny.Prettifier import prettify

import DB
import  config as cfg
data = DB.get_all_aneks_with_data()
#print(data)
cnter =0
for anek in data:
    print(cnter)
    cnter+=1
    text = anek["text"]
    likes = str(anek["likes"])
    hash = anek["hash"]
    if(int(likes) > 400):
        f = open("../"+cfg.path +"nice/"+ str(hash),"w")
    else:
        f = open("../"+cfg.path + "notnice/" + str(hash), "w")
    f.write(prettify(text))


