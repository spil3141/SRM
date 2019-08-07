# -*- coding: utf-8 -*-

""" Loading Dataset and Dividing into Train and Test """
import pandas,numpy
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
path_dataset = "../dataset"
X_data = []
Y_data = []
for i in os.listdir(os.path.join(src_dir,path_dataset)):
    print "Loading " + i 
    X_data.append(numpy.vstack((pandas.read_csv("../dataset/" + i).iloc[:,1:].values)))
    Y_data.append(numpy.vstack((pandas.read_csv("../dataset/" + i).iloc[:,:1].values)))
X_data= numpy.asarray(X_data)
Y_data = numpy.asarray(Y_data)
