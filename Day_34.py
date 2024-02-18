# DAY_34: Dictionary Methods in Python

"""
Dictionary Methods in Python:
Dictionaries in Python come with a variety of built-in methods that allow for easy manipulation and management of dictionary elements. These methods provide functionality for adding, updating, removing, and accessing dictionary elements.

"""

# Example: Dictionary Methods
# Creating dictionaries
ep1 = { 
    122: 45,
    123: 67,
    124: 78,
    125: 69
} 

ep2 = {
    222: 76,
    156: 90
}

# Merging dictionaries using the update() method
ep1.update(ep2)
print(ep1)

# Clearing dictionary elements using the clear() method
ep1.clear()
print(ep1)

# Removing a specific key-value pair using the pop() method
ep1 = { 
    122: 45,
    123: 67,
    124: 78,
    125: 69
} 
ep1.pop(122)
print(ep1)

# Removing the last inserted key-value pair using the popitem() method
ep1.popitem()
print(ep1)

# Deleting the entire dictionary using the del keyword
del ep2
# print(ep2)  # Raises NameError as ep2 is deleted

# Deleting a specific key-value pair using the del keyword
del ep1[122]
print(ep1)
