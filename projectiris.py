# David O'Brien 15-04-18

# Find the maximum value of each column
with open("data/iris.csv") as f:  # we are opening the file in this line. "as f" means we have called this file f from now on
  for line in f:
    line = line.split(',')
    print(max(line[0], line[1], line[2], line[3])) 

 

# Find the minimum value of each column



# Find the mean value of each column



# Find the median value of each column