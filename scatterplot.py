# David O'Brien 2018-04-17

#import the numpy package

import numpy

# read data file into array.

data = numpy.genfromtxt('data/iris.csv', delimiter=',')   # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html


sepallength = data[:,0]      # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the first column of data
sepalwidth = data[:,1]
petallength = data[:,2]
petalwidth = data[:,3]



# import the matplotlib.pyplot package

import matplotlib.pyplot as pl

# create scatter plot of sepal length vs sepal width for all specie types

pl.scatter(sepallength, sepalwidth)
pl.show()

# create scatter plot of petal length vs petal width for all specie types

pl.scatter(petallength, petalwidth)
pl.show()

