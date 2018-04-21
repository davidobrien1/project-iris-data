# Programming and Scripting

## Semester 1 Project 2018 - Fisher's Iris Data Set

### Student:    David O'Brien
### Student ID: G00364766

### Fisher's Iris Data Set Description

Fisher's Iris Data set is a multivariate data set introduced by the British statistician Ronald Fisher [4](https://en.wikipedia.org/wiki/Iris_flower_data_set)

### Summary Statistics of the Data Set

Description | Sepal Length | Sepal Width | Petal Length | Petal Width
----------- | ------------ | ----------- | ------------ | ------------
Minimum Value | 4.3 | 2.0 | 1.0 | 0.1
Maximum Value | 7.9 | 4.4 | 6.9 | 2.5
Mean Value | 5.843 | 3.054 | 3.759 | 1.199
Median Value | 5.8 | 3.0 | 4.35 | 1.3
Standard Deviation | 0.825 | 0.432 | 1.759 | 0.761

**Histograms**

![Histogram of Sepal Length](https://github.com/davidobrien1/project-iris-data/blob/master/Images/1%20-%20Histogram-Sepal%20Length.png)

![Histogram of Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/2%20-%20Histogram-Sepal%20Width.png)

![Histogram of Petal Length](https://github.com/davidobrien1/project-iris-data/blob/master/Images/3%20-%20Histogram%20-%20Petal%20Length.png)

![Histogram of Petal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/4%20-%20Histogram%20-%20Petal%20Width.png)

**Scatter Plots**

![Scatter Plot of Sepal Length vs Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/5%20-%20Scatter%20-%20Sepal%20Lenth%20vs%20Sepal%20Width.png)

![Scatter Plot of Petal Length vs Petal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/6%20-%20Scatter%20-%20Petal%20Lenth%20vs%20Petal%20Width.png)

![Colour Scatter Plot of Sepal Length vs Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/7%20-%20Colour%20Scatter%20-%20Sepal%20Lenth%20vs%20Sepal%20Width.png)

![Colour Scatter Plot of Sepal Length vs Sepal Width](https://github.com/davidobrien1/project-iris-data/blob/master/Images/8%20-%20Colour%20Scatter%20-%20Petal%20Length%20vs%20Petal%20Width.png)

**Matrix Plot**

![Matrix Plot of all variables](https://github.com/davidobrien1/project-iris-data/blob/master/Images/9%20-%20Matrix%20Plot.png)


### Use of Python libraries and other modules

**Numpy**

**Matplotlib.pyplot**

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
  - [x] Try to change the formatting of the graphs, include formatting in the code rather than applying in the image afterward
  - [ ] Try to create matrix of graphs 

**3 - Other analyses of the Iris data set**
- [ ] Example 1
- [ ] Example 2
- [ ] Example 3

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
- [ ] Matplotlib
- [ ] Numpy

**8 - Creating the Readme file**
- [x] Discuss how the Readme file was created

**9 - Use of Github**
- [ ] Github
- [ ] iPython
- [ ] Item 3

**10 - References**
- [ ] Double check that use of data is licensed and referenced


**11 - Review**
- [ ] Review all project items for any errors and improvements
