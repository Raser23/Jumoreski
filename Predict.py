from sklearn.externals import joblib

def load():
    global clf
    clf = joblib.load('Tengen_Toppa_mega_faggot.pkl')
dataLoaded = False

import VK as vk

def predict(txt):
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
