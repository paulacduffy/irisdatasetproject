import pandas as pd
import numpy as np
#Import pandas & numpy libraries

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
print (dataset.describe())

#Reference https://stackoverflow.com/questions/44594249/cannot-import-data-in-python-using-pandas for help loading dataset using pandas
#Prints mean, standard deviation, minimum value, 25th percentile, 50th percentile, 75th percentile & maximum values for each column
