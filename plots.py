import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Import pandas & numpy libraries

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

dataset.hist
plt.show()
#Histograms of each column
#Reference https://medium.com/codebagng/basic-an

dataset.boxplot (by = "class")
plt.show()
#Boxplot of each column by Class

