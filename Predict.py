from sklearn.externals import joblib
clf = joblib.load('Tengen_Toppa_mega_faggot.pkl')

import VK as vk

def predict(txt):
    result = clf.predict([txt])[0]
    return result

def PredictUser(userId):

    id = vk.GetUserById(userId)[0]['uid']
    print(id)
    groups = vk.textUserGroups( vk.GetUserGroups(id))
    return predict(groups)


print(PredictUser("alekseifilin"))