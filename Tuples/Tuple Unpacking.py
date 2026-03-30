"""Problem 5: Tuple Unpacking
1 Given student = ('Alice',21,'Computer Science',3.75).
2 Unpack the tuple into name, age, major, gpa.
3 Print a formatted statement describing the student."""

#1
student=('Alice',21,'Computer Science',3.75)

#2
name,age,major,gpa=student

#3
print(f"{name} is {age} years old, studying {major} with a GPA of {gpa}.")
