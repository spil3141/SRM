# -*- coding: utf-8 -*-

""" Loading .cvs Datasets from files """
import pandas
import numpy
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
path_dataset = "../dataset"
X = []
y = []
for i in os.listdir(os.path.join(src_dir,path_dataset)):
    print "Loading " + i 
    X.append(numpy.asarray(pandas.read_csv("../dataset/" + i).iloc[:,1:].values))
    y.append(numpy.asarray(pandas.read_csv("../dataset/" + i).iloc[:,:1].values))

X = numpy.vstack(([ i for i in X]))
y = numpy.vstack(([ i for i in y]))

""" Separating Training set and Testing set """

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size = 0.2,
        random_state= 1,
        stratify=y
        )


""" Applying Feature Scaling """
from sklearn.preprocessing import StandardScaler 

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)


"""Training a Support Vector Machine Classifier """

""" Model 1 : Using a Support Vector Machine Algorithm """
from sklearn.svm import SVC
model = SVC(kernel="rbf",
            C=100.0,
            gamma = 0.1, # 
            random_state=1)



model.fit(X_train_std,y_train)

""" Testing the performance of trained model """
from sklearn.metrics import accuracy_score 

y_pred = model.predict(X_test_std)
print "Accuracy: %.2f" % accuracy_score(y_test,y_pred)


""" Model Serialization/ Saving the Model for Future Use """
import joblib 
joblib.dump(model, "../Trained_Models/SVC_Version_0.1.sav")


 