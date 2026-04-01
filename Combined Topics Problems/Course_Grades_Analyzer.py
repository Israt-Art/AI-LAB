"""Problem 15: Course Grades Analyzer
1 Given courses = {'Alice':[85,90,78],'Bob':[70,75,80],'Charlie':[92,88,95]}.
2 Compute each student's average score using NumPy.
3 Store averages in a new dictionary.
4 Create a list of students whose average > 85.
5 Store the top student and their score in a tuple."""

import numpy as np

courses = {
    'Alice': [85, 90, 78],
    'Bob': [70, 75, 80],
    'Charlie': [92, 88, 95]
}

averages = {}

for student, scores in courses.items():
    avg = float(np.mean(scores))
    averages[student] = avg

print("Averages:", averages)

top_students = [student for student, avg in averages.items() if avg > 85]
print("Students with average > 85:", top_students)

top_student = max(averages, key=averages.get)
top_tuple = (top_student, averages[top_student])

print("Top student and score:", top_tuple)






