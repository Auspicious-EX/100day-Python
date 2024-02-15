# DAY_22: Introduction to Lists in Python

"""
Python Lists:
- Lists are ordered collections of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable, meaning we can alter them after creation.

Types of List Operations:
1. Indexing:
   - Positive Indexing: Accessing elements from the start of the list. Indexing starts from 0.
   - Negative Indexing: Accessing elements from the end of the list. Indexing starts from -1.

2. Slicing:
   - Slicing allows accessing a range of elements from a list.
   - Syntax: list[start:end:step]
   - start: Starting index of the slice (inclusive, default is 0)
   - end: Ending index of the slice (exclusive, default is the length of the list)
   - step: Step value for slicing (default is 1)

3. List Comprehension:
   - List comprehension is a concise way to create lists in Python.
   - It provides a compact syntax for creating new lists based on existing iterables.

"""

# Example 1: Creating a list
lst = [3, 5, 6]
print(lst)
print(type(lst))

# Example 2: Accessing elements of a list using positive indexing
print(lst[0])
print(lst[1])
print(lst[2])

# Example 3: Accessing elements of a list using negative indexing
lst = [1, 2, 3, "no"]
print(lst[-4])
print(lst[-3])
print(lst[-2])
print(lst[-1])

# Example 4: Checking if an item exists in a list
if 7 in lst:
    print("Yes")
else:
    print("No")

# Example 5: Applying 'in' operator on strings
if "Shu" in "Shubham":
    print("Yes")
else:
    print("No")

# Example 6: Iterating through a list
for item in lst:
    print(item)

# Example 7: Slicing a list
lst = [1, 2, 3, 4, 5]
print(lst[0:3])
print(lst[:3])
print(lst[0:])
print(lst[0:-1])
print(lst[0:3:2])

# Example 8: Using list comprehension to create new lists
squares = [i * i for i in range(4)]
print(squares)

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
names_with_o = [item for item in names if "o" in item]
print(names_with_o)

long_names = [item for item in names if len(item) > 4]
print(long_names)
