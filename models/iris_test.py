from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
import numpy as np

filename = 'model_1.sav'

iris = datasets.load_iris()
gnb = GaussianNB()

a = iris.data[:]
b = iris.target[:]
aa = a[:25]
ab = a[25:50]
ba = a[50:75]
bb = a[75:100]
ca = a[100:125]
cb = a[125:150]
xx = b[:25]
xy = b[25:50]
yx = b[50:75]
yy = b[75:100]
zx = b[100:125]
zy = b[125:150]

x_features = np.concatenate((aa,ba,ca))
y_features = np.concatenate((ab,bb,cb))
x_labels = np.concatenate((xx,yx,zx))
y_labels = np.concatenate((xy,yy,zy))



gnb.fit(x_features, x_labels)

joblib.dump(gnb,filename)

#.predict(iris.data)
#print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
