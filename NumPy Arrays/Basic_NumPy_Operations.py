"""Problem 9: Basic NumPy Operations
1 Create a NumPy array with values [10,20,30,40,50].
2 Multiply each element by 2.
3 Find the mean of the array.
4 Find the maximum value."""

import numpy as np 

#1
arr = np.array([10, 20, 30, 40, 50])

# 2
arr_multiplied = arr * 2
print("Array multiplied by 2:", arr_multiplied)

# 3
mean_value = arr.mean()
print("Mean of the array:", mean_value)

# 4
max_value = arr.max()
print("Maximum value:", max_value)