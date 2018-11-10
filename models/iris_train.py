from sklearn.externals import joblib
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()

model = joblib.load('model_1.sav')

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

y_features = np.concatenate((ab,bb,cb))
y_labels = np.concatenate((xy,yy,zy))

predictions = model.predict(y_features)
print (y_labels)
print (predictions)
print("score : %d" % ((y_labels == predictions).sum()))



#print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
