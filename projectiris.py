# David O'Brien 15-04-18

# Find the maximum value of each row
with open("data/iris.csv") as f:  # we are opening the file in this line. "as f" means we have called this file f from now on
  for line in f:                  # looping through the lines in the file
    line = line.split(',')
    print (max(line[0], line[1], line[2], line[3]))   # this prints the max value of each line


 

# Find the minimum value of each row
with open("data/iris.csv") as f:  # we are opening the file in this line. "as f" means we have called this file f from now on
  for line in f:                  # looping through the lines in the file
    line = line.split(',')        # here, i split the line before the print function
    print (min(line[0], line[1], line[2], line[3]))   # this prints the min value of each line


# Find the mean value of each column



# Find the median value of each column