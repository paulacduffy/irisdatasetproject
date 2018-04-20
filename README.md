# irisdatasetproject
Programming &amp; Scripting Project 2018

The Iris Flower Dataset was introduced by Ronald Fischer in his 1936 paper *The use of multiple measurements in taxonomic problems*. It is a multivariate dataset, which means that it contains two or more variable quantities. It contains the following data on 50 samples from each of three varieties of the Iris flower: 
Sepal Length (cm) 
Sepal Width (cm) 
Petal Length (cm) 
Petal Width (cm)  
Class (Iris Setosa, Iris Versicolour and Iris Virginica. 
(Reference: https://en.wikipedia.org/wiki/Iris_flower_data_set)
The sepal is the outer part of the flower that encloses a developing bud (often green in colour) and the petal is the coloured part of the flower. (Reference: https://www.amnh.org/learn/biodiversity_counts/ident_help/Parts_Plants/parts_of_flower.htm)
Investigating the dataset might involve trying to determine patterns in the data in relation to the three distinct classifications, i.e. does the data clearly show differences between the three classes.  A goal in analying a dataset such as this might be to determine if one could identify the class out of the three given the four measurements. 

My initial file is called Prelim.py. In this file I used the with statement to read the data, and attempted to do some analysis by column. The script prints the first column only. I couldn't find a way to perform the mathematical functions I wanted to, and after some investigation online I figured out that it is necessary to use libraries to manipulate the data as required. 

In the file Prelimstats.py I used Pandas to import the dataset, and perform some initial investigation. The first piece of script in this file imports the data and gives titles to the columns. 
The second script uses a simple pandas command to print the mean, standard deviation, minimum value, 25th, 50th & 75th percentiles & maximum values for each column.
The third script prints the number of rows & columns in the dataset.
The fourth script prints the number of rows of data for each class.
All of these scripts use the pandas library.

In the file Plots.py I imported matplotlib to create some graphs.

Histogram:
x axis is interval length, y axis is number of instances for each interval length
![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Dataset%20Histograms.png)

Boxplots for each feature grouped by Class
![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Dataset%20Boxplot%20grouped%20by%20class.png)
From the boxplots we can see the following:
1. The Iris Virginica has the longest sepal & longest petal 
2. The Iris Virginica also has the widest petal
3. The Iris Setosa has the widest sepal
4. The Iris Versicolor is in the middle in every measurement, i.e. it has neither the longest nor the shortest of any measurement
5. Petal length is the measurement that varies the most between the three classes
6. Sepal width is the measurement that varies the least between the three classes

![Histogram](https://github.com/paulacduffy/irisdatasetproject/blob/master/Iris%20Scatterplot%20with%20colours%20Sepal%20width%20vs%20length.png)
