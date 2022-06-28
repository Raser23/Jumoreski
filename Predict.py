#from sklearn.externals import joblib

def load():
    global clf
    #clf = joblib.load('Tengen_Toppa_mega_faggot.pkl')
dataLoaded = False

import VK as vk

def predict(txt):
    global dataLoaded
    if(not dataLoaded):
        load()
        dataLoaded = True
    result = clf.predict([txt])[0]
    return result

def PredictUser(userId):

    id = vk.GetUserById(userId)[0]['uid']
    print(id)
    groups = vk.textUserGroups( vk.GetUserGroups(id))
    return predict(groups)

def Answer(message):
    txt = message.text.split(" ")
    #if (len(txt) == 1):
    return 'Пока не работает'
    '''else:

        userId = txt[1]
        if '/' in txt[1]:
            p = txt[1].split('/')
            userId = p[-1]

        result = PredictUser(userId)
        resultStr = ""
        if (result == 0):
            resultStr = "Говноед"
        else:
            resultStr = "Не говноед"
        return resultStr'''