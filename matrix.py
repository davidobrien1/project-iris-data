# David O'Brien 2018-04-21
# Code taken from https://seaborn.pydata.org/examples/scatterplot_matrix.html

# Import matplotlib

import matplotlib.pyplot as pl

# Import seaborn

import seaborn as sns 


sns.set(style="ticks")    # this sets the syle

df = sns.load_dataset("iris") # this line is looking for online csv files on https://github.com/mwaskom/seaborn-data:  https://stackoverflow.com/questions/30336324/seaborn-load-dataset/30337377
sns.pairplot(df, hue="species")   # this plots pairwise relationships in a dataset: https://seaborn.pydata.org/generated/seaborn.pairplot.html

pl.show()   # This shows the scatter last plot created

