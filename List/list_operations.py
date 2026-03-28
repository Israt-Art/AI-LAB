"""Problem 1: List Operations
1 Create a list containing the numbers 5, 12, 7, 3, 18, 9.
2 Append 15 to the list.
3 Insert 20 at index 2.
4 Remove the element 7 from the list.
5 Sort the list in descending order and print the final list.
"""


numbers=[5,12,7,3,18,9]

numbers.append(15)

numbers.insert(2,20)

numbers.remove(7)

numbers.sort(reverse=True)

print(numbers)
