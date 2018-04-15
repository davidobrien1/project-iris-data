# David O'Brien 15-04-18


import numpy

# read data file into array.

data = numpy.genfromtxt('data/iris.csv', delimiter=',')   # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy


# Find the minimum value of each column

firstcol = data[:,0]      # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the first column of data
meanfirstcol = numpy.min(data[:,0]) # https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html - used this link to find mean and changed to min to get minimum value
meansecondcol = numpy.min(data[:,1])
meanthirdcol = numpy.min(data[:,2])
meanfourthcol = numpy.min(data[:,3])

print("Min. Sepal Length = ", meanfirstcol)
print("Min. Sepal Width = ", meansecondcol) 
print("Min. Petal Length = ", meanthirdcol)
print("Min. Sepal Width = ", meanfourthcol)





# Find the maximum value of each column


# Find the mean value of each column



# Find the median value of each column