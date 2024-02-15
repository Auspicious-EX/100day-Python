# DAY_24: Tuples in Python

"""
Python Tuples:
- Tuples are ordered collections of data items.
- They store multiple items in a single variable.
- Tuple items are separated by commas and enclosed within round brackets ().
- Tuples are unchangeable meaning we cannot alter them after creation.

Tuple Indexes:
- Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], the second item has index [1], the third item has index [2], and so on.

Accessing Tuple Items:
I. Positive Indexing:
   - Tuple items can be accessed using their indexes.
II. Negative Indexing:
   - Negative indexing is used to access items from the end of the tuple. The last item has index [-1], the second last item has index [-2], the third last item has index [-3], and so on.
III. Check for Item:
   - The 'in' keyword can be used to check if a given item is present in the tuple.
IV. Range of Index (Slicing):
   - A range of tuple items can be accessed by specifying the start, end, and step values.

"""

# Example: Creating and accessing tuples
tup = (1, 2, 3, 4, 5)
print(tup, type(tup))

# Example: Tuple indexing
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

# Example: Accessing tuple items using slicing
print("Here", tup[0:3])
print("Here", tup[0:-3])

# Example: Length of a tuple
print(len(tup))

# Example: Accessing the last item of a tuple using negative indexing
print(tup[-1])

# Example: Checking if an item exists in the tuple
if 3 in tup:
    print("Yes")

# Example: Slicing a tuple to create a new tuple
tup2 = tup[1:4]
print(tup2)
