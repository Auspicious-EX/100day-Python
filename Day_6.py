# DAY 6 : Variables and Data Types

print("\nVariable")
""" 
Variables:
    - Variables are containers for storing data values.
    - Variables do not need to be declared with any particular type and can even change type after they have been set.
    
    Rules of defining Variable
        - A variable name must start with a letter or the underscore character.
        - A variable name cannot start with a number.
        - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
        - Variable names are case-sensitive (age, Age and AGE are three different variables).
    
Example:
"""

a = 10
print("\na=10\nHere \'a\' is a variable which is store the value\n")



print("\nDatatypes:")
""" 
Data Types:
    - Data types are the classification or categorization of data items.
    - It represents the kind of value that tells what operations can be performed on a particular data.
    - Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.
    
Types:

1. Text type (String):
    - str
    - Strings in python are surrounded by either single quotation marks, or double quotation marks.
    - 'hello' is the same as "hello".
    - You can display a string literal with the print() function.
    
2. Numaric Types
    →	int: Used for storing integer numbers.
        - Example:
            a = 10
    →	float: Used for storing floating-point (decimal) numbers.
        - Example:
            a = 10.5
    →	complex: Used for storing complex numbers.
        - Example:
            a = 3+5j
            
3. Sequence Types
    →	list: Used for storing a list of values. List can contain elements of different data types.
        - Example:
            a = [1, 2, 3, 4, 5]
    →	tuple: Used for storing a list of values. Tuple can contain elements of different data types.
        - Example:
            a = (1, 2, 3, 4, 5)
    →	range: Used for generating a sequence of numbers.
        - Example:
            a = range(1, 10)

4. Mapping Type
    →	dict: Used for storing a key-value pair.
        - Example:
            a = {'name': 'John', 'age': 25}
            
5. Set Types
    →	set: Used for storing a sequence of immutable objects. Set cannot contain duplicate values.
        - Example:
            a = {1, 2, 3, 4, 5}
    →	frozenset: Used for storing a sequence of immutable objects. Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
        - Example:
            a = frozenset({1, 2, 3, 4, 5})

6. Boolean type (bool):
    - bool: Used for storing True or False.
        - Example:
            a = True
            b = False
            
7. Binary Types:
    →	bytes: Used for storing a sequence of bytes. It is an immutable version of bytearray object.
        - Example:
            a = b"Hello"
    →	bytearray: Used for storing a sequence of bytes. It is a mutable version of bytes object.
        - Example:
            a = bytearray(5)
    →	memoryview: Used for accessing the internal data of an object that supports the buffer protocol.
        - Example:
            a = memoryview(bytes(5))
                
"""

# We can chack data type using type() function

print("\nText type(String):")

a = "Shubham"
print("a = ", a, " and type(a) = ", type(a))


print("\nNumaric Types:")

a = 10
print("a = ", a, " and type(a) = ", type(a))

a = 10.5
print("a = ", a, " and type(a) = ", type(a))

a = 3+5j
print("a = ", a, " and type(a) = ", type(a))


print("\nSequence Types:")
a = [1, 2, 3, 4, 5]
print("a = ", a, " and type(a) = ", type(a))

a = (1, 2, 3, 4, 5)
print("a = ", a, " and type(a) = ", type(a))

a = range(1, 10)
print("a = ", a, " and type(a) = ", type(a))


print("\nMapping Type:")
a = {'name': 'John', 'age': 25}
print("a = ", a, " and type(a) = ", type(a))

print("\nSet Type:")
a = {1, 2, 3, 4, 5}
print("a = ", a, " and type(a) = ", type(a))

a = frozenset({1, 2, 3, 4, 5})
print("a = ", a, " and type(a) = ", type(a))

print("\nBoolean Type:")
a = True
print("a = ", a, " and type(a) = ", type(a))

a = False
print("a = ", a, " and type(a) = ", type(a))


print("\nBinary Types:")
a = b"Hello"
print("a = ", a, " and type(a) = ", type(a))
a = bytearray([65, 66, 67])
print("a = ", a, " and type(a) = ", type(a))
a = memoryview(bytes(5))
print("a = ", a, " and type(a) = ", type(a))


