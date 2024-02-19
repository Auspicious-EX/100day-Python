# DAY_36: Exception Handling in Python

""" 
Exception Handling:
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. It deals with these events to avoid program or system crashes.

Exceptions in Python:
Python has many built-in exceptions that are raised when your program encounters an error. When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

Python try...except:
try...except blocks are used in Python to handle errors and exceptions. The code inside the try block runs normally, and if an error occurs, it's caught by the except block.

Syntax:
try:
    # Code that could potentially raise an exception
except:
    # Handling code for the exception
"""

# Example 1: Handling invalid input for the multiplication table
a = input("Enter the number: ")
print(f"Multiplication table of {a}:")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")

except Exception as e:
    print("Invalid input")

print("Some lines of code")
print("End of program")

# Example 2: Handling ValueError and IndexError
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error")
