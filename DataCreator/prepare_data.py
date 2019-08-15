import DataCreator.TextPrettifier as tp
import DB
import re
js = DB.get_all_aneks(sort=0)
f = open('j.txt', 'w')
for raw_string in js:
    #print(raw_string)
    if(len(raw_string) < 40):
        continue


    formatted_string = tp.pret(raw_string)
    print(formatted_string)

    senteces = re.compile("[.!?\n]").split(formatted_string) #re.split("[.!?\n]", formatted_string)
    for sent in senteces:
        if len(sent)>1:
            f.write(sent.strip())
            f.write('.\n')
    #print(senteces)
    #f.write(formatted_string)
    #f.write('\n')
f.close()