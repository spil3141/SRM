from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

filename = 'model_1.sav'

iris = datasets.load_iris()
gnb = GaussianNB()

x_features = iris.data[:100]
x_labels = iris.target[:100]
y_features = iris.data[100:]
y_label = iris.target[100:]

#print(x_features.shape)
#print(x_labels.shape)
#print(y_features.shape)
#print(y_labels.shape)

gnb.fit(x_features, x_labels)

joblib.dump(gnb,filename)

print (y_features[0])
print (y_label[0])

#.predict(iris.data)
#print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
