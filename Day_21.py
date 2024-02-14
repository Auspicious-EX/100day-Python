# DAY_21: Function Arguments in Python

"""
Function Arguments in Python:
- Functions in Python can accept different types of arguments, including positional arguments, keyword arguments, default arguments, variable-length arguments, and keyword-only arguments.
- These arguments provide flexibility in how functions can be called and used.

Types of Function Arguments:
1. Positional Arguments: Arguments passed to a function based on their position.
2. Keyword Arguments: Arguments passed with their corresponding parameter names.
3. Default Arguments: Arguments with default values specified in the function definition.
4. Variable-Length Arguments (*args): Allows a function to accept any number of positional arguments.
5. Keyword-Only Arguments (*, kwargs): Requires arguments to be passed as keyword arguments after the * symbol.
"""

# Example 1: Function with default arguments
def average(a=9, b=1):
    """
    Calculates the average of two numbers.

    Args:
    a (int): First number (default is 9)
    b (int): Second number (default is 1)
    """
    print("AVG:", (a + b) / 2)

# Example 2: Function with keyword arguments
average(b=9)

# Example 3: Function with keyword arguments in different order
average(b=9, a=21)

# Example 4: Function with variable-length arguments
def avera(*nums):
    """
    Calculates the average of multiple numbers.

    Args:
    *nums (int): Variable-length argument list
    """
    total = sum(nums)
    print("AVG:", total / len(nums))

avera(2, 3)

# Example 5: Function with return value
def ave(a, b, c=3):
    """
    Calculates the average of three numbers.

    Args:
    a (int): First number
    b (int): Second number
    c (int): Third number (default is 3)

    Returns:
    float: Average of the three numbers
    """
    return (a + b + c) / 3

result = ave(2, 3)
print("Average:", result)





""" 
Function Arguments and return statement
There are four types of arguments that we can provide in a function:

Default Arguments
Keyword Arguments
Variable length Arguments
Required Arguments



Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.


Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.


Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.


Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.


Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

return Statement
The return statement is used to return the value of the expression back to the calling

 """
