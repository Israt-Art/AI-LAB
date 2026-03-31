"""Problem 10: Matrix Creation
1 Create a 3x3 NumPy matrix with values from 1 to 9.
2 Print the second row.
3 Print the third column.
4 Compute the sum of all elements."""

import numpy as np


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("3x3 Matrix:\n", matrix)


second_row = matrix[1]  
print("Second row:", second_row)


third_column = matrix[:, 2]  
print("Third column:", third_column)


total_sum = matrix.sum()
print("Sum of all elements:", total_sum)