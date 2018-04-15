# David O'Brien 15-04-18
# Project Iris Data Analysis


#import the numpy package


import numpy

# read data file into array.

data = numpy.genfromtxt('data/iris.csv', delimiter=',')   # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy


firstcol = data[:,0]      # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the first column of data
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

# import the matplotlib.pyplot library

import matplotlib.pyplot as pl  # taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.hist(firstcol)               # plots a histogram of the first column of data. taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8

pl.hist(secondcol)               # plots a histogram of the first column of data. taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8

pl.hist(thirdcol)               # plots a histogram of the first column of data. taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8

pl.hist(fourthcol)               # plots a histogram of the first column of data. taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8