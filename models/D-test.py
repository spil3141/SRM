from sklearn import datasets
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import numpy as np

digits = datasets.load_digits()

y_test = digits.data[:100]
y_labels = digits.target[:100]

model = joblib.load('D-R-model2.sav')

prediction = model.predict(y_test)

score = (y_labels == prediction).sum()
total = prediction.size

print ( str(score) + ":" + str(total))
