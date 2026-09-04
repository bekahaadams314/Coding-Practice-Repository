import numpy as np 
# boolean masking requires satisfying during a specific condition

# create a 1D array containing numbers from 1 to 10 
arr = np.arange(1,11) # range from 1 to 10 inclusive

# create a boolean mask to find all odd numbers 
odd_numbers = arr[arr%2 != 0] # this checks for odd numbers 
even_numbers = arr[arr%2 == 0] # this checks for even numbers 

print("Odd Numbers:", odd_numbers)

# replace all odd numbers in the original array with -1
arr[arr%2 != 0] = -1 
print("Modified array:", arr)