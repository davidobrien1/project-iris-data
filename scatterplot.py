# David O'Brien 2018-04-17

#import the numpy package

import numpy

# read data file into array.  Using numpy.genfromtext, i was able to load the code numpy.genfromtxt('data/iris.csv', delimiter=',') 
# and this was fine for creating the basic scatter plots, but when it came to creating different colour data points
# for the different species, it was not picking up the 5th column and converting it to color
# I received the 'nan' error regularly which means not a number.  I know I needed to Python to read this column as a string.
# To investigate this I started looking through the different parameters of numpy.genfromtext at https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html
# I found the 'usecols' and 'dtype' parameters and was able to use this to set the data types for the first 4 columns and then the 5th column

data = numpy.genfromtxt('data/iris.csv', delimiter=',', usecols=(0, 1, 2, 3), dtype=float)   # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html


sepallength = data[:,0]      # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the first column of data
sepalwidth = data[:,1]
petallength = data[:,2]
petalwidth = data[:,3]

species = numpy.genfromtxt('data/iris.csv', delimiter=',', usecols=(4), dtype=str)


# import the matplotlib.pyplot package

import matplotlib.pyplot as pl

# create scatter plot of sepal length vs sepal width for all specie types

pl.scatter(sepallength, sepalwidth)
pl.show()

# create scatter plot of petal length vs petal width for all specie types

pl.scatter(petallength, petalwidth)
pl.show()

# create scatter plot of sepal length vs sepal width for all specie types showing the specie types in different colours

#setting colors for each flower type

color_dict = { 'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}

pl.scatter(sepallength, sepalwidth, color=[ color_dict[i] for i in species ] )

pl.show()