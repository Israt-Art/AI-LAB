"""Problem 2: List Slicing
1 Given numbers = [2,4,6,8,10,12,14,16].
2 Extract the first four elements.
3 Extract the last three elements.
4 Extract elements from index 2 to 5.
5 Reverse the list using slicing.
6 Extract every second element."""

numbers = [2, 4, 6, 8, 10, 12, 14, 16]


first_four = numbers[:4]
print("First four:", first_four)


last_three = numbers[-3:]
print("Last three:", last_three)


index_2_to_5 = numbers[2:6]
print("Index 2 to 5:", index_2_to_5)


reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)


every_second = numbers[::2]
print("Every second element:", every_second)