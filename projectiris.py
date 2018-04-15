# David O'Brien 15-04-18
# Project Iris Data Analysis


#import the numpy package

import numpy

# read data file into array.

data = numpy.genfromtxt('data/iris.csv', delimiter=',')   # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy

# Find the minimum value of each column

firstcol = data[:,0]      # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the first column of data
minfirstcol = numpy.min(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html - used this link to find mean and changed to min to get minimum value
minsecondcol = numpy.min(data[:,1])
minthirdcol = numpy.min(data[:,2])
minfourthcol = numpy.min(data[:,3])

print("Min. Sepal Length = ", minfirstcol)
print("Min. Sepal Width = ", minsecondcol) 
print("Min. Petal Length = ", minthirdcol)
print("Min. Sepal Width = ", minfourthcol)

# Find the maximum value of each column

maxfirstcol = numpy.max(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html - used this link to find mean and changed to max to get maximum value
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxfourthcol = numpy.max(data[:,3])

print("Max. Sepal Length = ", maxfirstcol)
print("Max. Sepal Width = ", maxsecondcol) 
print("Max. Petal Length = ", maxthirdcol)
print("Max. Sepal Width = ", maxfourthcol)

# Find the mean value of each column

meanfirstcol = numpy.mean(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html - used this link to find mean
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanfourthcol = numpy.mean(data[:,3])

print("Mean Sepal Length = ", meanfirstcol)
print("Mean Sepal Width = ", meansecondcol) 
print("Mean Petal Length = ", meanthirdcol)
print("Mean Sepal Width = ", meanfourthcol)

# Find the median value of each column

medianfirstcol = numpy.median(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html - used this link to find median
mediansecondcol = numpy.median(data[:,1])
medianthirdcol = numpy.median(data[:,2])
medianfourthcol = numpy.median(data[:,3])

print("Median Sepal Length = ", medianfirstcol)
print("Median Sepal Width = ", mediansecondcol) 
print("Median Petal Length = ", medianthirdcol)
print("Median Sepal Width = ", medianfourthcol)