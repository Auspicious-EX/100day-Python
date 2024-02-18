# DAY_31: Sets in Python

"""
Sets in Python:
Sets are unordered collections of unique elements in Python. They are used to store multiple items in a single variable. Sets are defined by enclosing the elements within curly braces {}.

Features of Sets:
1. Unordered: Sets do not maintain any order for their elements.
2. Unique Elements: Sets contain only unique elements. Duplicate elements are automatically removed.
3. Immutable: Sets are mutable, meaning their elements cannot be changed once they are created.

"""

# Example: Creating and Using Sets
S = {2, 4, 3, 4}
print(S)
print(type(S))

# Creating an empty set
Shubham = set()
print(Shubham)
print(type(Shubham))

# Creating a set with different data types
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
