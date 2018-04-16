#Paula Duffy
#Iris Dataset Preliminary Statistics

import pandas as pd
#Import pandas library

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
#Import Dataset
#Reference https://stackoverflow.com/questions/44594249/cannot-import-data-in-python-using-pandas for help loading dataset using pandas

print (dataset.describe())
#Prints mean, standard deviation, minimum value, 25th percentile, 50th percentile, 75th percentile & maximum values for each column


print ("The number of rows & columns in the dataset are", (dataset.shape))
#dimensions of the dataset


print (dataset.groupby('class').size() )
#Number of rows of data for each class

