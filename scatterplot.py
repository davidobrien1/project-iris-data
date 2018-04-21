# David O'Brien 2018-04-17

#import the numpy package

import numpy

# read data file into array.  Using numpy.genfromtext, i was able to load the code numpy.genfromtxt('data/iris.csv', delimiter=',') 
# and this was fine for creating the basic scatter plots, but when it came to creating different colour data points
# for the different species, it was not picking up the 5th column and converting it to color
# I received the 'nan' error regularly which means not a number.  I know I needed Python to read this column as a string.
# To investigate this I started looking through the different parameters of numpy.genfromtext at https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html
# I found the 'usecols' and 'dtype' parameters and was able to use this to set the data types for the first 4 columns and then the 5th column

data = numpy.genfromtxt('data/iris.csv', delimiter=',', usecols=(0, 1, 2, 3), dtype=float)    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html

# Set the names of the first four columns

sepallength = data[:,0]       # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the first column of data
sepalwidth = data[:,1]        # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the second column of data
petallength = data[:,2]       # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the third column of data
petalwidth = data[:,3]        # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the fourth column of data

# read column 5 of the data file into an array and tell Python the the 5th column data type is a string

species = numpy.genfromtxt('data/iris.csv', delimiter=',', usecols=(4), dtype=str)    # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html


# import the matplotlib.pyplot package

import matplotlib.pyplot as pl

# create scatter plot of sepal length vs sepal width for all specie types

pl.scatter(sepallength, sepalwidth)   # You can also add marker sizes, colours, scales, line widths, edge colour sof markers etc.. https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html
pl.title('Scatter Plot of Sepal Length Vs. Sepal Width ')      # Went to the following link to find the '.title' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.xlabel('Sepal Length') # Went to the following link to find the '.xlabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.ylabel('Sepal Width')  # Went to the following link to find the '.ylabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.show()   # This shows the scatter last plot created

# create scatter plot of petal length vs petal width for all specie types

pl.scatter(petallength, petalwidth)
pl.title('Scatter Plot of Petal Length Vs. Petal Width ')      # Went to the following link to find the '.title' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.xlabel('Petal Length') # Went to the following link to find the '.xlabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.ylabel('Petal Width')  # Went to the following link to find the '.ylabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.show()   # This shows the scatter last plot created

# setting colors for each flower type

color = { 'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}

# create scatter plot of sepal length vs sepal width for all specie types showing the specie types in different colours

pl.scatter(sepallength, sepalwidth, color=[ color[i] for i in species ] )    # Found code at this link that helped created colour the data points per species: https://stackoverflow.com/questions/27318906/python-scatter-plot-with-colors-corresponding-to-strings
pl.title('Scatter Plot of Sepal Length Vs. Sepal Width ')      # Went to the following link to find the '.title' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.xlabel('Sepal Length') # Went to the following link to find the '.xlabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.ylabel('Sepal Width')  # Went to the following link to find the '.ylabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.figlegend(('Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'),scatterpoints=1,loc='lower left',ncol=3,fontsize=8)
pl.show()   # This shows the scatter last plot created