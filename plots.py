#Paula Duffy Programming & Scripting Project
#Histogram & Boxplot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Import pandas, numpy & matplotlib libraries

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

#Histograms of each column
#Reference https://medium.com/codebagng/basic-an
dataset.hist
plt.show()

#Boxplot of each column by Class
dataset.boxplot (by = "class")
plt.show()

#Scatterplot of ratio of sepal length to sepal width
dataset.plot(kind="scatter", x="sepal-length", y="sepal-width")
plt.show()
#reference: http://www.learn4master.com/machine-learning/visualize-iris-dataset-using-python
