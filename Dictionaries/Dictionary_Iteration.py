"""Problem 7: Dictionary Iteration
1 Given marks = {'Math':85,'Physics':78,'Chemistry':82,'Biology':74}.
2 Print all subjects and marks.
3 Find the subject with the highest marks.
4 Calculate the average marks."""

#1
marks = {'Math': 85, 'Physics': 78, 'Chemistry': 82, 'Biology': 74}

# 2
for subject, score in marks.items():
    print(subject, ":", score)

# 3
highest_subject = max(marks, key=marks.get)
print("\nHighest Marks Subject:", highest_subject, "-", marks[highest_subject])

# 4
average = sum(marks.values()) / len(marks)
print("Average Marks:", average)




#another way

marks = {'Math': 85, 'Physics': 78, 'Chemistry': 82, 'Biology': 74}

# 2
subjects = list(marks.keys())

for i in range(len(subjects)):
    subject = subjects[i]
    score = marks[subject]
    print(subject, ":", score)

# 3
highest_subject = subjects[0]
for i in range(1, len(subjects)):
    if marks[subjects[i]] > marks[highest_subject]:
        highest_subject = subjects[i]
print("\nHighest Marks Subject:", highest_subject, "-", marks[highest_subject])

# 4
total = 0
for i in range(len(subjects)):
    total += marks[subjects[i]]
average = total / len(subjects)
print("Average Marks:", average)
