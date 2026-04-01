"""Problem 12: Student Records System
1 Given students = [('Alice',85),('Bob',72),('Charlie',90),('David',65),('Eva',88)].
2 Convert the data into a dictionary where name is the key.
3 Create a list of students who scored above 80.
4 Calculate the average score using NumPy."""


import numpy as np


students = [('Alice',85),('Bob',72),('Charlie',90),('David',65),('Eva',88)]

# 2
student_dict = dict(students)
print("Dictionary:", student_dict)

# 3
above_80 = [name for name, score in students if score > 80]
print("Students with score > 80:", above_80)

# 4
scores = np.array([score for name, score in students])
average = np.mean(scores)
print("Average score:", average)