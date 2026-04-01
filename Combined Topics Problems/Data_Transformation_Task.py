"""Problem 16: Data Transformation Task
1 Given data = [('A',[10,20,30]),('B',[5,15,25]),('C',[12,18,24])].
2 Convert the structure into a dictionary.
3 Convert each value list into a NumPy array.
4 Compute the mean of each array.
5 Store results in a new dictionary."""
   
import numpy as np


data = [('A', [10, 20, 30]), ('B', [5, 15, 25]), ('C', [12, 18, 24])]

# 2
data_dict = dict(data)
print("Step 2 - Dictionary:", data_dict)

# 3
for key in data_dict:
    data_dict[key] = np.array(data_dict[key])
print("Step 3 - NumPy arrays:", data_dict)

# 4 & 5
mean_dict = {key: float(np.mean(arr)) for key, arr in data_dict.items()}
print("Step 5 - Means:", mean_dict)