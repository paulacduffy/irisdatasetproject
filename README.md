# irisdatasetproject
**Programming &amp; Scripting Project 2018**

The Iris Flower Dataset was introduced by Ronald Fischer in his 1936 paper *The use of multiple measurements in taxonomic problems*. It is a multivariate dataset, which means that it contains two or more variable quantities. It contains the following data on 50 samples from each of three varieties of the Iris flower: 
* Sepal Length (cm); 
* Sepal Width (cm); 
* Petal Length (cm); 
* Petal Width (cm); and  
* Class (*Iris setosa*, *Iris versicolour* and *Iris virginica*). 

Fischer developed a model to distinguish the species from each other based on a combination of the four features.
(Reference: https://en.wikipedia.org/wiki/Iris_flower_data_set)
The sepal is the outer part of the flower that encloses a developing bud (often green in colour) and the petal is the coloured part of the flower. (Reference: https://www.amnh.org/learn/biodiversity_counts/ident_help/Parts_Plants/parts_of_flower.htm)

In order to investigate a dataset one needs to establish what purpose the dataset fulfils and determine what specific questions need to be asked of the data. Investigating this particular dataset might involve trying to determine patterns in the data in relation to the three distinct classifications, i.e. does the data clearly show differences between the three classes.  A goal in analying a dataset such as this might be to determine if one could identify which class a flower belongs to given the four measurements. 

My initial file is [Prelim.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/Prelim.py). In this file I used the with statement to read the data, and attempted to do some analysis by column. The script prints the first column only. I couldn't find a way to perform the mathematical functions I wanted to, and after some investigation online I figured out that it is necessary to use libraries to manipulate the data as required. 

In the file [Prelimstats.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/prelimstats.py) I used Pandas to import the dataset, and perform some initial investigation. The first piece of script in this file imports the data and gives titles to the columns. 
The second script uses a simple pandas command to print the mean, standard deviation, minimum value, 25th, 50th & 75th percentiles & maximum values for each column.

* Mean is another term for the average, i.e. add up each value & divide by the number of values
* Standard Deviation is the amount the values differ from the average, i.e. a low standard deviation indicates that the data points tend to be close to the mean; whereas a high standard deviation indicates that the datapoints are spread out over a wide range of values.
* Minimum value is self-explanatory.
* 25th percentile is the value below which 25% of the observations are found;
* 50th percentile is the value below which 50% of the observations are found; and
* 75th percentile is the value below which 75% of the observations are found.
* Maximum value is also self-explanatory.

From the data we can see that the petal length measurement has the greatest standard deviation, while the sepal width has the lowest.

The third script prints the number of rows & columns in the dataset.
The fourth script prints the number of rows of data for each class.
All of these scripts use the pandas library.

In the file [Plots.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/plots.py) I imported matplotlib to create some graphs as follows:

Histogram:
A histogram shows the number of instances of each interval represented by the height of the bars. 
x axis is interval length, y axis is number of instances for each interval length. The sepal width histogram most resembles a normal distribution, i.e. points are as likely to occur on one side of the average as the other. The petal width & petal length histograms might suggest that one species can be separated from the other two by these measurements, as there are two distinct peaks in these diagrams.

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Dataset%20Histograms.png)

Boxplots:
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

In the file [scatterplot.py](https://github.com/paulacduffy/irisdatasetproject/blob/master/scatterplot.py) I used the seaborn library to create scatterplots distinguishing the three species by colour as follows:

Scatterplot showing sepal width vs sepal length colour coded by species:

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Scatterplot.png)

This scatterplot shows that the species *Iris setosa* can be distinguished clearly from the other two species by it's sepal width vs length ratio. The other two species cannot be clearly distinguished from each other by these measurements.

Scatterplot showing petal width vs petal length colour coded by species:
![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Scatterplot%20petal%20iris.png)

Similary, this scatterplot shows that the *Iris setosa* can also be distinguished clearly from the other two species by it's petal width vs length ratio. The other two species can't be distinuished clearly from each other by this ratio.
When I started to compare petal width and sepal width, and petal length and sepal length I started to see some distinction between all three species:

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Scatterplot%20petal%20length%20sepal%20length%20iris.png)

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Scatterplot%20petal%20width%20sepal%20width%20iris.png)

As we can see from these scatterplots the *Iris setosa* is still the most clearly distinguishable from the other two species, but the *Iris virginica* & *Iris versicolor* can be distinguished from each other using these ratios.


