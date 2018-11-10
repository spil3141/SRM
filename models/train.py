from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np 
from sklearn.externals import joblib

filename = 'SRM_2.sav'
data1 = pd.read_csv("../dataset/dataset-A.csv")
data2 = pd.read_csv("../dataset/dataset-B.csv")
data3 = pd.read_csv("../dataset/dataset-C.csv")
data4 = pd.read_csv("../dataset/dataset-D.csv")
data5 = pd.read_csv("../dataset/dataset-E.csv")

data = np.vstack((data1.values,data2.values,data3.values,data4.values,data5.values))

x_features = data[:,1:]
x_labels = data[:,:1]
x_labels = np.reshape(x_labels,-1)

#print ( x_labels.ndim)

clf = GaussianNB()
clf.fit(x_features,x_labels)

joblib.dump(clf,filename)

