# David O'Brien 2018-04-17

#import the numpy package

import numpy

# read data file into array.

data = numpy.genfromtxt('data/iris.csv', delimiter=',')   # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy

sepallength = data[:,0]
sepalwidth = 
petallength =
Petalwidth = 


#import the matplotlib package

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()