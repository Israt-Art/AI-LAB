"""Problem 11: Array Filtering
1 Given arr = np.array([5,12,7,20,3,15,8]).
2 Extract elements greater than 10.
3 Replace all values less than 10 with 0."""

import numpy as np

arr=np.array([5,12,7,20,3,15,8])

greater_than_10=arr[arr>10]
print("Element greater than 10:",greater_than_10)

arr[arr<10]=0
print("Updated array:",arr)