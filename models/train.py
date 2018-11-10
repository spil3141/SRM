import pandas as pd
import numpy as np 
data1 = pd.read_csv("../dataset/dataset-A.csv")
data2 = pd.read_csv("../dataset/dataset-B.csv")
data3 = pd.read_csv("../dataset/dataset-C.csv")
data4 = pd.read_csv("../dataset/dataset-D.csv")
data5 = pd.read_csv("../dataset/dataset-E.csv")

data = np.concatenate(data1,data2,data3,data4,data5)