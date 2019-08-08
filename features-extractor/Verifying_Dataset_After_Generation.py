import pandas as pd
data = pd.read_csv("../dataset/dataset-.csv")
print(data.shape)



"""

import csv,numpy

f = open('data.csv', 'rb+')
buf = csv.reader(f, delimiter=',')
numpy.asarray(buf)
print(type(buf))
f.close()

"""