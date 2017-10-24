
import config as cfg
from sklearn.datasets import load_files
twenty_train = load_files("../"+cfg.path,shuffle=True, random_state=42)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts.shape)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


from sklearn.grid_search import GridSearchCV
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
               'tfidf__use_idf': (True, False),
               'clf__alpha': (1e-2, 1e-3),
}

from sklearn.linear_model import SGDClassifier

from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()),
                      ('clf', SGDClassifier(loss='hinge', penalty='l2',  alpha = 1e-3, n_iter = 5, random_state = 42)),
])
"""
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(twenty_train.data[:400], twenty_train.target[:400])
best_parameters, score, _ = max(gs_clf.grid_scores_, key=lambda x: x[1])

for param_name in sorted(parameters.keys()):
     print("%s: %r" % (param_name, best_parameters[param_name]))

docs_test = twenty_train.data
_ = text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)


from sklearn import metrics
print(metrics.classification_report(twenty_train.target, predicted, target_names=twenty_train.target_names))
"""
from sklearn.externals import joblib
joblib.dump(text_clf, 'Tengen_Toppa_mega_faggot.pkl')