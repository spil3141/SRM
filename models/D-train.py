from sklearn import datasets
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
filename = 'D-R-model2.sav'

digits = datasets.load_digits()

x_train = digits.data[:]
x_labels = digits.target[:]

clf = GaussianNB()

clf.fit(x_train,x_labels)

joblib.dump(clf,filename)


