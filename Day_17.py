# Day_17: For Loops in Python

""" 
Introduction to Loops
Loops allow a programmer to execute a group of statements a certain number of times. Two main types of loops are:
- for loop
- while loop

- The for Loop
for loops iterate over a sequence of iterable objects in Python. Iterating over a sequence involves strings, lists, tuples, sets, and dictionaries.

"""

# Using the range function to generate a sequence of numbers.
# range(start, stop, step)
# start: Optional. Default is 0 if not specified.
# stop: Required. Specifies the endpoint of the sequence (exclusive).
# step: Optional. Specifies the increment (or decrement if negative).
for i in range(1, 10):
    print(i)

name = "Shubham"
for char in name:
    print(char)
    if char == "b":
        print("Here is b")

colors = ["Red", "Green", "Yellow"]

for color in colors:
    print(color)
    for char in color:
        print(char)

# Looping through a range of numbers
a = range(20000)
for num in a:
    print(num + 1)

# Looping through a range of numbers with a step of 5
a = range(0, 20001, 5)
for num in a:
    print(num)