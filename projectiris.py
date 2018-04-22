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
print("Min. Petal Width = ", minfourthcol)

# Find the maximum value of each column

maxfirstcol = numpy.max(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html - used this link to find mean and changed to max to get maximum value
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxfourthcol = numpy.max(data[:,3])

print("Max. Sepal Length = ", maxfirstcol)
print("Max. Sepal Width = ", maxsecondcol) 
print("Max. Petal Length = ", maxthirdcol)
print("Max. Petal Width = ", maxfourthcol)

# Find the mean value of each column

meanfirstcol = numpy.mean(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html - used this link to find mean
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanfourthcol = numpy.mean(data[:,3])

print("Mean Sepal Length = ", meanfirstcol)
print("Mean Sepal Width = ", meansecondcol) 
print("Mean Petal Length = ", meanthirdcol)
print("Mean Petal Width = ", meanfourthcol)

# Find the median value of each column

medianfirstcol = numpy.median(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html - used this link to find median
mediansecondcol = numpy.median(data[:,1])
medianthirdcol = numpy.median(data[:,2])
medianfourthcol = numpy.median(data[:,3])

print("Median Sepal Length = ", medianfirstcol)
print("Median Sepal Width = ", mediansecondcol) 
print("Median Petal Length = ", medianthirdcol)
print("Median Petal Width = ", medianfourthcol)

# Find the standard deviation of each column

stdfirstcol = numpy.std(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html - used this link to find median
stdsecondcol = numpy.std(data[:,1])
stdthirdcol = numpy.std(data[:,2])
stdfourthcol = numpy.std(data[:,3])

print("Standard Deviation Sepal Length = ", stdfirstcol)
print("Standard Deviation Width = ", stdsecondcol) 
print("Standard Deviation Length = ", stdthirdcol)
print("Standard Deviation Width = ", stdfourthcol)


# Use pandas to create a summary table of the data in the iris data set

import pandas as pd   #importing pandas
ir = pd.DataFrame(data) # https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis
print(ir.describe())    # using the pandas.DataFrame.describe to create table of data set https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html 

