from sklearn.externals import joblib

model = joblib.load('model_1.sav')


print (model.predict([[6.3,3.3,6.0,2.5]]))
#print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
