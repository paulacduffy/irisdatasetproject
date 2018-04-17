import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Import pandas, numpy & matplotlib libraries

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

#Scatterplot of sepal length & sepal width
dataset.plot(kind="scatter", x="sepal-length", y="sepal-width")
plt.show()