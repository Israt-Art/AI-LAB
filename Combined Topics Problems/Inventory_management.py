"""Problem 13: Inventory Management
1 Given inventory = {'apple':[10,1.5],'banana':[25,0.8],'orange':[15,1.2],'mango':[8,2.0]}.
2 Calculate the total value of each item.
3 Store results in a new dictionary.
4 Use NumPy to compute the average item value."""

import numpy as np


inventory = {
    'apple': [10, 1.5],
    'banana': [25, 0.8],
    'orange': [15, 1.2],
    'mango': [8, 2.0]
}


total_value = {}
for item, (quantity, price) in inventory.items():
    total_value[item] = quantity * price

print("Total value of each item:", total_value)


values_array = np.array(list(total_value.values()))
average_value = np.mean(values_array)

print("Average item value:", average_value)