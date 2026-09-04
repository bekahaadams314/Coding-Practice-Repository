import numpy as np

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

# extract and print the center element (recall indexing starts at 0 not 1)
print("Center Element:", matrix[1,1])

# extract and print the entire second row
print("Entire Second Row:", matrix[1,:])

# extract and print the last two columns as a sub-array 
print("Last Two Columns:", matrix[:,1:])