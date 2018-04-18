# David O'Brien 2018-04-17

#import the numpy package

import numpy

# read data file into array.

data = numpy.genfromtxt('data/iris.csv', delimiter=',')   # https://stackoverflow.com/questions/3518778/how-to-read-csv-into-record-array-in-numpy

sepallength = data[:,0]
sepalwidth = data[:,1]
petallength = data[:,2]
petalwidth = data[:,3]
species = data[:,4]

#import the matplotlib package

import matplotlib.pyplot as pl

pl.scatter(sepallength, sepalwidth, color='r')

pl.show()

#

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris = pd.read_csv("data/iris.csv")
sns.jointplot(x="5.1", y="3.5", data=iris, size=5)
sns.FacetGrid(iris, hue="Iris-setosa", size=5).map(plt.scatter, "5.1", "3.5").add_legend()
