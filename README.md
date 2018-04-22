# Programming and Scripting

## Semester 1 Project 2018 - Fisher's Iris Data Set

### Student:    David O'Brien
### Student ID: G00364766

### Fisher's Iris Data Set Description

Fisher's Iris Data set is a multivariate data set introduced by the British statistician Ronald Fisher [4](https://en.wikipedia.org/wiki/Iris_flower_data_set)

### Summary Statistics of the Data Set

The table below shows some summary statistics of the Iris Data set.  This information was obtained by running the code in the file projectiris.py

Description | Sepal Length | Sepal Width | Petal Length | Petal Width
----------- | ------------ | ----------- | ------------ | ------------
Count | 150 | 150 | 150 | 150
Minimum Value | 4.3 | 2.0 | 1.0 | 0.1
Maximum Value | 7.9 | 4.4 | 6.9 | 2.5
Mean Value | 5.843 | 3.054 | 3.759 | 1.199
Median Value | 5.8 | 3.0 | 4.35 | 1.3
Standard Deviation | 0.825 | 0.432 | 1.759 | 0.761
25% | 5.1 | 2.8 | 1.6 | 0.3
50% | 5.8 | 3.0 | 4.35 | 1.3
75% | 6.4 | 3.3 | 5.1 | 1.8


**Histograms**

The following histograms were created using the code in pihist.py.

![Histogram of Sepal Length](https://github.com/davidobrien1/project-iris-data/blob/master/Images/1%20-%20Histogram-Sepal%20Length.png)

![Histogram of Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/2%20-%20Histogram-Sepal%20Width.png)

![Histogram of Petal Length](https://github.com/davidobrien1/project-iris-data/blob/master/Images/3%20-%20Histogram%20-%20Petal%20Length.png)

![Histogram of Petal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/4%20-%20Histogram%20-%20Petal%20Width.png)

**Scatter Plots**

The following scatter plots were created using the code in scatterplot.py.

![Scatter Plot of Sepal Length vs Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/5%20-%20Scatter%20-%20Sepal%20Lenth%20vs%20Sepal%20Width.png)

![Scatter Plot of Petal Length vs Petal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/6%20-%20Scatter%20-%20Petal%20Lenth%20vs%20Petal%20Width.png)

![Colour Scatter Plot of Sepal Length vs Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/7%20-%20Colour%20Scatter%20-%20Sepal%20Lenth%20vs%20Sepal%20Width.png)

![Colour Scatter Plot of Sepal Length vs Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/8%20-%20Colour%20Scatter%20-%20Petal%20Length%20vs%20Petal%20Width.png)

**Matrix Plot**

The following matrix plots were created using the code in matrix.py.

![Matrix Plot of all variables](https://github.com/davidobrien1/project-iris-data/blob/master/Images/9%20-%20Matrix%20Plot.png)


### Use of Python libraries and other modules

**Numpy**

NumPy is the fundamental package for scientific computing with Python [26](http://www.numpy.org/).  In this project, I used numpy.genfromtxt to read the data file into an array.  Using different parameters within this function, I was able to load specific columns (usecols) and convert each one to the appropriate data type (dtype).  numpy.genfromtext is able to perform many other useful actions to data including; dealing with blank data, skipping headers and footers, skipping lines.

**Matplotlib**

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms [27](https://matplotlib.org/).  In this project, I used matplotlib.pyplot to various types of graphs of the iris data set.  Using different parameters within this function, I was able to plot histograms (matplotlib.pyplot.hist), label the graph (matplotlib.pyplot.title/xlabel/ylabel) and show the graph (matplotlib.pyplot.show).  

**Seaborn**

Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics [28](https://seaborn.pydata.org/).  In this project, I used seaborn to matrix plot of the iris data set.  Using different parameters within this function, I was able to set the style (seaborn.set), load the data set from a github repoitory (seaborn.load_dataset) and plot pairwise relationships in the dataset (seaborn.pairplot).  Note that the code for this was taken directly from reference [29](https://seaborn.pydata.org/examples/scatterplot_matrix.html).  I found it very useful that this module was able to create such a detailed graph with little coding. 


### How to run the Python Code and what it does

To run any of the files below in python, type "filename.py" in the integrated terminal

This can also be run in ipython by going to the directory of the file and typing "run filename.py"

CTRL+Shift+b will also run this file in python provided you have created the "tasks.json" as described in previous videos.  See image below for this:

![Image of .json script](https://github.com/davidobrien1/project-iris-data/blob/master/Images/tasks.json%20snip.PNG)

**projectiris.py**

The [projectiris.py](https://github.com/davidobrien1/project-iris-data/blob/master/projectiris.py) file uses the numpy package to calculate the different summary values in the summary table above.

**pihist.py**

The [pihist.py](https://github.com/davidobrien1/project-iris-data/blob/master/pihist.py) file uses the matplotlib package to create different graphs of the data.

**scatterplot.py**

The [scatterplot.py](https://github.com/davidobrien1/project-iris-data/blob/master/scatterplot.py) file uses the matplotlib package to create different graphs of the data.

**matrix.py**

The [matrix.py](https://github.com/davidobrien1/project-iris-data/blob/master/matrix.py) file uses the seaborn package to create a matrix of plots of the iris data.

### Data Files

Note that the Fisher's Iris data file is located [here](https://github.com/davidobrien1/project-iris-data/tree/master/Data)

### Creating the Readme file

As the first part of this project involved creating the project plan within the Readme file, I found myself researching various formatting syntax for Markdown files.  Much of the information found online seems to be repetitive and I found that the references in [2](https://guides.github.com/features/mastering-markdown/) and [3](https://help.github.com/articles/basic-writing-and-formatting-syntax/) below cover much of the information I required for this project.

### Other analyses of the Iris Data set

The analysis of the Iris data set used in reference [30](https://guides.github.com/features/mastering-markdown/) by Ritvik Raj uses multiple modules for Python including sys, scipy, numpy, matplotlib, pandas, and scikit-learn.  The data set is loaded directly from the UCI machine learning repository as opposed to my method of downloading the file locally (except where i am creating the matrix plot using seaborn).

The dataset summary includes additional information to my summary including the count and percentiles of the different types of data.  On further research, I learnt that the pandas.dataframe.describe library is able to provide this information very easily and have therefore added this data to the summary table using the pandas library.

Ritvik uses histograms and box plots to represent that data.

The data is then split into two sets, one to train the model and the other as a validation set

Different statistical methods are then used to find patterns between the variables in the dataset and the results from the algorithms are then compared.  

### References

Search terms used - iris data set, fisher's iris data set, iris flower data set, multivariate data set, Anderson's iris data set, Ronald Fisher, iris data set analysis, scatter plot numpy, matplotlib scatter plot example, sort csv columns into arrays python, matplotlib multiple array scatter plot, plot data points in different colors matplotlib, matplotlib scatter color by value

1 - https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis

2 - https://guides.github.com/features/mastering-markdown/ 

3 - https://help.github.com/articles/basic-writing-and-formatting-syntax/ 

4 - https://en.wikipedia.org/wiki/Iris_flower_data_set

5 - https://archive.ics.uci.edu/ml/datasets/iris

6 - https://gist.github.com/curran/a08a1080b88344b0c8a7

7 - https://matplotlib.org/faq/usage_faq.html

8 - https://docs.python.org/3/tutorial/

9 - http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

10 - https://stackoverflow.com/questions/35329573/finding-max-value-in-a-column-of-csv-file-python

11 - https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy

12 - https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html

13 - https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html

14 - https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html

15 - https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/

16 - http://benalexkeen.com/scatter-charts-in-matplotlib/

17 - https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

18 - http://www.learn4master.com/machine-learning/visualize-iris-dataset-using-python

19 - https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html

20 - https://matplotlib.org/2.0.0/examples/index.html

21 - https://stackoverflow.com/questions/33790909/plotting-points-with-different-colors-by-name-in-matplotlib

22 - https://stackoverflow.com/questions/27318906/python-scatter-plot-with-colors-corresponding-to-strings

23 - https://matplotlib.org/api/pyplot_api.html

24 - https://stackoverflow.com/questions/30336324/seaborn-load-dataset/30337377

25 - https://github.com/mwaskom/seaborn-data

26 - http://www.numpy.org/

27 - https://matplotlib.org/

28 - https://seaborn.pydata.org/

29 - https://seaborn.pydata.org/examples/scatterplot_matrix.html

30 - https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/

31 - https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis



**-------------------------------------------------------------------------------------------**

# Project Plan Check List

**1 - Researching the data set**
- [ ] What investigating a data set entails
- [ ] How can Python be used to do this?
- [ ] What does the data contain?
- [ ] The background surrounding it
- [ ] Why is this data talked about so much when it comes to data analytics

**2 - Investigation of the Iris data set**
- [x] Download the Iris data set
- [ ] Summary Statistics
  - [x] Max. value of each column
  - [x] Min. value of each column
  - [x] Mean value of each column
  - [x] Median of each column
  - [x] Standard deviations
  - [x] Histogram of different columns 
  - [x] Use pandas to create summary table of data
  - [x] Try to change the formatting of the graphs, include formatting in the code rather than applying in the image afterward
  - [x] Try to create matrix of graphs 

**3 - Other analyses of the Iris data set**
- [x] [Ritvik Raj](https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/)


**4 - Write a summary of the investigations including tables and graphs**
- [x] Table of summary stats
- [x] Histograms of individual columns
- [x] Scatter plots of multiple columns
- [x] Scatter plots of multiple columns with coloured data points

**5 - Update Project Plan as research progresses and additional information becomes apparent**
- [ ] Consider any new information learned as part of the project plan

**6 - How to run the Python code and what it does**
- [x] pihist.py
- [x] projectiris.py
- [x] scatterplot.py

**7 - Use of Python libraries and other modules**
- [x] Matplotlib
- [x] Numpy
- [x] Seaborn

**8 - Creating the Readme file**
- [x] Discuss how the Readme file was created

**9 - Use of other resources**
- [ ] Github
- [ ] iPython

**10 - References**
- [ ] Double check that use of data is licensed and referenced


**11 - Review**
- [ ] Review all project items for any errors and improvements
