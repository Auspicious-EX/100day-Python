# DAY_42: Enumerate Function in Python

marks = [7, 4, 5, 6, 10, 5, 3, 2, 4, 9]

""" 
Enumerate function in Python:
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.

Syntax:
for index, value in enumerate(sequence):
    # Body of the loop

Usage:
The enumerate function returns a tuple containing the index and value of each element in the sequence. You can use a for loop to unpack these tuples and assign them to variables.
 """

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

""" 
Changing the start index:
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function.
 """

index = 0
for mark in marks:
    print(mark)
    if index == 4:
        print("He is shubham")
    index += 1

# Enumerate with a specified start index
for index, mark in enumerate(marks, start=0):
    print(index, mark)
    if index == 4:
        print("He is shubham")
    index += 1

""" 
Looping over a list with enumerate and formatting output:
You can use enumerate to loop over a list and format the output, such as displaying the index along with the value.
 """

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index + 1}: {fruit}')

# Extra example: Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
