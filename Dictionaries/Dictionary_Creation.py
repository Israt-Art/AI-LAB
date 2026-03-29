"""Problem 6: Dictionary Creation
1 Create a dictionary containing name, age, department, cgpa.
2 Print all keys and values.
3 Update the cgpa value.
4 Add a new key called 'university'."""


#1
student={
    "name":"Alice",
    "age":21,
    "department":"Computer Science",
    "cgpa":3.75
}

#2
print("keys:",student.keys())
print("values:",student.values())

#3
student["cgpa"]=3.90

#4
student["university"]="XYZ University"

#5
print("\nUpdated Dictionary:",student)