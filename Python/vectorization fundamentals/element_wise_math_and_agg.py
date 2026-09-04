import numpy as np 

# create two arrays: 
a = np.array([2, 4, 3])
b = np.array([9, 5, 8])

# also create two matricies for reference
A = np.array([[2, 1], 
              [1, 3]])

B = np.array([[5], 
              [5]])

# matrix multiplication 
multiplied_matrix = a*b

# matrix division (left division)
divided_matrix = np.linalg.solve(a,b) # right division, inv

matrix1 = np.array([[10, 20], 
                    [30, 40]])

matrix2 = np.array([[2, 5], 
                    [3, 4]])

# element wise matrix division 
result = matrix1/matrix2

# manupulate matrix using a scalar 
c = 5
bigger = c*matrix1
scaled_down = matrix1/c

# print
print("Sum:", np.sum(multiplied_matrix))
print("Mean:", np.mean(multiplied_matrix))
print("Max:", np.max(multiplied_matrix))

# For the assessments, we should focus on: 
# 1. vectorized thinking vs. loops 
# 2. under the hood theory
# 3. geometric brownian motion, portfolio at risk 
# portfolio value at risk 
# linear regression from scratch 
# numpy practice moving forward: https://codesolid.com/numpy-practice-questions-to-make-you-an-expert/
# finite element methods: https://www.simscale.com/forum/t/the-finite-element-method-fundamentals-matrix-algebra-3/28995