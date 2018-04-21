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
pl.title('Histogram of Sepal Length')      # Went to the following link to find the '.title' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.xlabel('Centimetres') # Went to the following link to find the '.xlabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.ylabel('Quantity')  # Went to the following link to find the '.ylabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8

pl.hist(secondcol)               # plots a histogram of the first column of data. taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.title('Histogram of Sepal Width')      # Went to the following link to find the '.title' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.xlabel('Centimetres') # Went to the following link to find the '.xlabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.ylabel('Quantity')  # Went to the following link to find the '.ylabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8

pl.hist(thirdcol)               # plots a histogram of the first column of data. taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.title('Histogram of Petal Length')      # Went to the following link to find the '.title' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.xlabel('Centimetres') # Went to the following link to find the '.xlabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.ylabel('Quantity')  # Went to the following link to find the '.ylabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8

pl.hist(fourthcol)               # plots a histogram of the first column of data. taken from 'Matplotlib Pyplot' video tutorial topic 8
pl.title('Histogram of Petal Width')      # Went to the following link to find the '.title' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.xlabel('Centimetres') # Went to the following link to find the '.xlabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.ylabel('Quantity')  # Went to the following link to find the '.ylabel' parameter to create a title for the scatter plot dhttps://matplotlib.org/api/pyplot_api.html
pl.show()                       # shows the last histogram.  taken from 'Matplotlib Pyplot' video tutorial topic 8