# DAY_33: Dictionaries in Python

"""
Dictionaries in Python:
Dictionaries are unordered collections of key-value pairs in Python. They are used to store and manipulate data in the form of key-value mappings. Dictionaries are defined by enclosing key-value pairs within curly braces {}.

Features of Dictionaries:
1. Key-Value Pairs: Dictionaries store data in the form of key-value pairs, where each key is associated with a value.
2. Unordered: Dictionaries do not maintain any order for their elements.
3. Mutable: Dictionaries are mutable, meaning their elements can be changed after creation.
4. Unique Keys: Keys in dictionaries must be unique. If duplicate keys are provided, the values associated with the latest occurrence of the key will be retained.

"""

# Example: Creating and Using Dictionaries
# Dictionary with string keys
dic = {
    "Name": "Shubham",
    "Age": 18
}
print(dic)

# Dictionary with integer keys
dic2 = {
    123: "Shubham",
    234: "Viny",
    345: "Rahul"
}
print(dic2)
print(dic2[234])

# Accessing dictionary elements
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info['name'])

# Handling missing keys
# print(info['name2'])  # Raises KeyError
print(info.get('name2'))  # Returns None if key does not exist

# Accessing keys and values
print(info.keys())
print(info.values())

# Iterating through dictionary keys
for key in info.keys():
    print(key, info[key])

# Iterating through dictionary items
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
