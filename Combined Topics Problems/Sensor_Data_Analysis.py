"""Problem 14: Sensor Data Analysis
1 Given temps = [22,24,19,23,25,18,21].
2 Convert the list into a NumPy array.
3 Find mean, max, and min temperature.
4 Store results in a dictionary.
5 Create a tuple containing (max_temp, min_temp)."""

import numpy as np

temps = [22, 24, 19, 23, 25, 18, 21]
temps_array = np.array(temps)

mean_temp = float(np.mean(temps_array))
max_temp = int(np.max(temps_array))
min_temp = int(np.min(temps_array))

results = {
    'mean': mean_temp,
    'max': max_temp,
    'min': min_temp
}

temp_tuple = (max_temp, min_temp)

print("Results dictionary:", results)
print("Tuple (max, min):", temp_tuple)