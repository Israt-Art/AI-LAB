"""Problem 4: Tuple Basics
1 Create a tuple containing five programming languages.
2 Print the first and last element.
3 Check whether 'Python' exists in the tuple.
4 Convert the tuple into a list and append 'Rust'."""

#1
languages=("Python","Java","C++","javascript","Go")

#2
print("First element:",languages[0])
print("Last element:",languages[-1])

#3
if "Python" in languages:
    print("Python exists in the tuple")
else:
    print("Python does not exist in the tuple")

#4
languages_list=list(languages)
languages_list.append("Rust")
print("Updated list:",languages_list)