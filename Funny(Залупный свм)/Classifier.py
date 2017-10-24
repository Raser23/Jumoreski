from sklearn.externals import joblib
clf = joblib.load('Funny(Залупный свм)/Tengen_Toppa_mega_faggot.pkl')

from Funny.Prettifier import prettify
def predict(txt):
    txt = prettify(txt)
    result = clf.predict([txt])[0]
    return result