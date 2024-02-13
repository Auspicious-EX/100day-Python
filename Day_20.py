# DAY_20: Functions in Python

"""
Functions in Python:
- A function is a block of reusable code that performs a specific task.
- It helps in organizing code into smaller, manageable pieces.
- Functions improve code reusability, readability, and maintainability.

Types of Functions:
1. Built-in Functions: Functions provided by Python.
2. User-defined Functions: Functions created by the user.

Function Components:
1. Function Name: Unique identifier for the function.
2. Parameters: Inputs to the function (optional).
3. Return Statement: Outputs from the function (optional).

"""

# Example 1: User-defined function to calculate geometric mean
def calculategmean(a, b):
    """
    Calculates the geometric mean of two numbers.
    
    Args:
    a (float): First number
    b (float): Second number
    
    Returns:
    float: Geometric mean of the two numbers
    """
    gmean = (a * b) / (a + b)
    print(gmean)

# Example 2: User-defined function to compare two numbers
def isgreater(a, b):
    """
    Compares two numbers and prints which one is greater.
    
    Args:
    a (int): First number
    b (int): Second number
    """
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")

# Example 3: Calling functions with different arguments
a = 9
b = 8
isgreater(a, b)
calculategmean(a, b)

a = 8
b = 74
isgreater(a, b)
calculategmean(a, b)

# Example 4: User-defined function with pass statement
def isless(a, b):
    """
    Placeholder function with pass statement.
    
    Args:
    a (any): First value
    b (any): Second value
    """
    pass
