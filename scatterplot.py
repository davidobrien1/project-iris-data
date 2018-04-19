# David O'Brien 2018-04-17

#import the numpy package

import numpy

# read data file into array.

data = numpy.genfromtxt('data/iris.csv', delimiter=',')   # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html


sepallength = data[:,0]      # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy - this lists all numbers in the first column of data
sepalwidth = data[:,1]
petallength = data[:,2]
petalwidth = data[:,3]
species = data[:,4]



# import the matplotlib.pyplot package

import matplotlib.pyplot as pl

# create scatter plot of sepal length vs sepal width for all specie types

pl.scatter(sepallength, sepalwidth)
pl.show()

# create scatter plot of petal length vs petal width for all specie types

pl.scatter(petallength, petalwidth)
pl.show()

# create scatter plot of sepal length vs sepal width for all specie types showing the specie types in different colours

pl.scatter(sepallength, sepalwidth, c= ["red", "green", "blue"])   #https://stackoverflow.com/questions/33790909/plotting-points-with-different-colors-by-name-in-matplotlib
pl.show()

# determine color
flower = species[i].decode("utf-8")
color = ""
if flower == "Iris-setosa":
	color = "red"
elif flower == "Iris-versicolor":
	color = "green"
elif flower == "Iris-virginica":
	color = "blue"

plt.scatter(x, y, s=scale, c=color, alpha=1, edgecolor="none")  #http://www.pybloggers.com/2015/09/my-first-time-using-matplotlib/
