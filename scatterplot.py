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
sns.lmplot(x="sepal-width", y="sepal-length", hue="class", data=dataset, legend_out = False)
plt.legend(loc = 'lower right')

sns.lmplot(x="petal-width", y="petal-length", hue="class", data=dataset, legend_out = False)
plt.legend(loc = 'lower right')

plt.show()
#reference: https://seaborn.pydata.org/examples/multiple_regression.html
#reference: https://stackoverflow.com/questions/27019079/move-seaborn-plot-legend-to-a-different-position