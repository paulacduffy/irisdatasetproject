import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
#Import pandas, numpy & matplotlib libraries

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)


#Scatterplot using Seaborn
sns.lmplot(x="sepal-width", y="sepal-length", hue="class", data=dataset)
plt.show()