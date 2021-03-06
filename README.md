# irisdatasetproject
## Programming &amp; Scripting Project 2018

The Iris Flower Dataset was introduced by Ronald Fischer in his 1936 paper *The use of multiple measurements in taxonomic problems*. It is a multivariate dataset, which means that it contains two or more variable quantities. It contains the following data on 50 samples from each of three varieties of the Iris flower: 
* Sepal Length (cm); 
* Sepal Width (cm); 
* Petal Length (cm); 
* Petal Width (cm); and  
* Class (*Iris setosa*, *Iris versicolour* and *Iris virginica*). 

Fischer developed a model to distinguish the species from each other based on a combination of the four features.
(Reference: https://en.wikipedia.org/wiki/Iris_flower_data_set)
The sepal is the outer part of the flower that encloses a developing bud (often green in colour) and the petal is the coloured part of the flower. (Reference: https://www.amnh.org/learn/biodiversity_counts/ident_help/Parts_Plants/parts_of_flower.htm).
The Iris Dataset is widely used in pattern recognition literature. Classification of the data would involve discovering patterns from examining the petal & sepal size of the flower. 

In order to investigate a dataset one needs to establish what purpose the dataset fulfils and determine what specific questions need to be asked of the data. Investigating this particular dataset might involve trying to determine patterns in the data in relation to the three distinct classifications, i.e. does the data clearly show differences between the three classes.  A goal in analying a dataset such as this might be to determine if one could identify which class a flower belongs to given the four measurements.

There are many examples of analsis of the Iris dataset available online, using various methods:
http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP386/IntroEDA-Iris.html - uses the R language;
http://msudatascience.com/blog/2016/8/27/quick-analysis-in-r-with-the-iris-dataset - also uses R;
https://www.maplesoft.com/support/help/maple/view.aspx?path=examples/IrisData - uses Maple;
https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-the-iris-data-set/ - uses IBM Watson Analytics; and there are many examples of analysis using Python:
http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf
https://www.kaggle.com/adityabhat24/iris-data-analysis-and-machine-learning-python
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
All of these examples have a lot in common. They begin with a simple investigation of the data to identify some statistics e.g. mean, maximum values etc. They then go on to visualise the data using various methods. Finally some of the analyses available go into predicting species depending on measurements. This [analysis](http://www.statlab.uni-heidelberg.de/data/iris/) separates the species based on petal & sepal areas, with only three misclassifications. In this project I will not be looking at predicting species type based on measurements, but will look at the other two areas mentioned: statistics for the dataset & visualisations of the data.

### Preliminary Analysis

My initial file is [Prelim.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/Prelim.py). In this file I used the with statement to read the data, and attempted to do some analysis by column. The script prints the first column only. I couldn't find a way to perform the mathematical functions I wanted to, and after some investigation online I figured out that it is necessary to use libraries to manipulate the data as required. 

In the file [Prelimstats.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/prelimstats.py) I used Pandas to import the dataset, and perform some initial investigation. The first piece of script in this file imports the data and gives titles to the columns. 
The second command prints the top 20 rows of data:

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Dataset%20top%2020%20rows.PNG)

The third command prints the mean, standard deviation, minimum value, 25th, 50th & 75th percentiles & maximum values for each column.

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Dataset%20description.PNG)

* Mean is another term for the average, i.e. add up each value & divide by the number of values
* Standard Deviation is the amount the values differ from the average, i.e. a low standard deviation indicates that the data points tend to be close to the mean; whereas a high standard deviation indicates that the datapoints are spread out over a wide range of values.
* Minimum value is self-explanatory.
* 25th percentile is the value below which 25% of the observations are found;
* 50th percentile is the value below which 50% of the observations are found; and
* 75th percentile is the value below which 75% of the observations are found.
* Maximum value is also self-explanatory.

From the data we can see that:
* Sepals are on average longer & wider than petals
* Petal width has the smallest minimum and maximum value
* Sepal length has the largest minimum and maximum value
* Petal length has the greatest standard deviation, i.e. has a large distribution from the mean; while the sepal width has the lowest standard deviation, i.e. a small distribution from the mean.

The fourth command prints the number of rows & columns in the dataset (150 rows and 5 columns).
The fifth command prints the number of rows of data for each class (50).
This file uses the pandas library.

### Visualisation of the data

In the file [Plots.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/plots.py) I imported matplotlib to create some graphs as follows:

**Histogram:**
A histogram shows the number of instances of each interval represented by the height of the bars. 
x axis is interval length, y axis is number of instances for each interval length. The sepal width histogram most resembles a normal distribution, i.e. points are as likely to occur on one side of the average as the other. The petal width & petal length histograms might suggest that one species can be separated from the other two by these measurements, as there are two distinct peaks in these diagrams.

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Dataset%20Histograms.png)

**Boxplot:**
The boxplot is a standardised way of showing the distribution of data based on maximum value, minimum value, first quartile, median, third quartile & outliers as shown below (Reference: https://datavizcatalogue.com/methods/box_plot.html):

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/box_plot.png)

The boxplots below show each measurement grouped by class: 

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Dataset%20Boxplot%20grouped%20by%20class.png)
From the boxplots we can see the following:
1. The *Iris virginica* has the longest sepal & longest petal 
2. The *Iris virginica* also has the widest petal
3. The *Iris setosa* has the widest sepal
4. The *Iris versicolor* is in the middle in every measurement, i.e. it has neither the longest nor the shortest of any measurement
5. Petal length is the measurement that varies the most between the three classes
6. Sepal width is the measurement that varies the least between the three classes

**Scatterplot:** In the file [scatterplot.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/scatterplot.py) I used the seaborn library to create scatterplots distinguishing the three species by colour as follows:

Scatterplot showing sepal width vs sepal length colour coded by species:

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Scatterplot.png)

This scatterplot shows that the species *Iris setosa* can be distinguished clearly from the other two species by it's sepal width vs length ratio. The other two species cannot be clearly distinguished from each other by these measurements.

Scatterplot showing petal width vs petal length colour coded by species:
![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Scatterplot%20petal%20iris.png)

Similary, this scatterplot shows that the *Iris setosa* can also be distinguished clearly from the other two species by it's petal width vs length ratio. The other two species can't be distinuished clearly from each other by this ratio.
When we compare petal width and sepal width, and petal length and sepal length we see some distinction between all three species:

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Scatterplot%20petal%20length%20sepal%20length%20iris.png)

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Scatterplot%20petal%20width%20sepal%20width%20iris.png)

As we can see from these scatterplots the *Iris setosa* is still the most clearly distinguishable from the other two species, but the *Iris virginica* & *Iris versicolor* can be distinguished a lot more from each other using these ratios with just a small number of overlaps.

### Conclusion
In conclusion, the species *Iris setosa* is the most clearly distinguishable from the other two species by either it's sepal length vs width ratio or petal length vs width ratio. The other two species cannot be distinguished from each other using these ratios, but using the ratios sepal width vs petal width and sepal length vs petal length can distinguish between the other two species.
I would like to do some further research to find out how to build a prediction model to identify species given measurements, but this is beyond my abilities at this stage!


