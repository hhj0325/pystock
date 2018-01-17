"""
page
    222
    225
    226
    227
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import datetime


def print_result(name, docs, predicted, trains):
    print(name)
    for doc, category in zip(docs, predicted):
        print('%r =>%s' % (doc, trains.target_names[category]))
    print('----')

categories = ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
twenty_train = fetch_20newsgroups(subset='train', categories=categories)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

docs_new = ['God is love', 'OpenGl on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

print(datetime.datetime.now())
predicted1 = NearestCentroid().fit(X_train_tfidf, twenty_train.target).predict(X_new_tfidf)
print_result('NearestCentroid', docs_new, predicted1, twenty_train)

print(datetime.datetime.now())
predicted2 = MultinomialNB().fit(X_train_tfidf, twenty_train.target).predict(X_new_tfidf)
print_result('MultinomialNB', docs_new, predicted2, twenty_train)

print(datetime.datetime.now())
predicted3 = KNeighborsClassifier(15).fit(X_train_tfidf, twenty_train.target).predict(X_new_tfidf)
print_result('KNeighborsClassifier', docs_new, predicted3, twenty_train)

print(datetime.datetime.now())
predicted4 = svm.SVC(kernel='linear').fit(X_train_tfidf, twenty_train.target).predict(X_new_tfidf)
print_result('svm.SVC', docs_new, predicted4, twenty_train)

print(datetime.datetime.now())












