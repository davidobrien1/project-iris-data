# David O'Brien 2018-04-17

#import the numpy package

import numpy

# read data file into array.

sepallength, sepalwidth, petallength, petalwidth, species = numpy.genfromtxt('data/iris.csv', delimiter=',',usecols=0,1,2,3,4)   # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html

# import the matplotlib.pyplot package

import matplotlib.pyplot as pl

# create scatter plot of sepal length vs sepal width for all specie types

pl.scatter(sepallength, sepalwidth)

