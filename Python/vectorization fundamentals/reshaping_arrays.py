import numpy as np 

# create a 1D array with values from 0 to 11
arr = np.arange(0,12) # create an array with values 0 to 11

# reshape this array into 2D array with 3 rows and four columns
arr_2d = arr.reshape(3,4)

# reshape the original array into 3D array with a shape of 2,2,3
arr_3d = arr.reshape(2,2,3) 

print("Original:\n", arr)
print("2D array:\n", arr_2d)
print("3D array:\n", arr_3d)