import pymorphy2
morph = pymorphy2.MorphAnalyzer()
def prettify(txt):
    symbols = ["0","1","2","3","4","5","6","7","8","9",".",",","!","@","\n","_","-","\u2013","_","-",":","\\","(",")","{","}","*","%","?","\"","№","#","$",";","%","  "]
    for s in symbols:
        while s in txt:
            txt = txt.replace(s," ")
    txt = txt.lower()
    txt = txt.split(" ")
    result = []
    for word in txt:
        result.append(morph.parse(word)[0].normal_form)

    return " ".join(result)

