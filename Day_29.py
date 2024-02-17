# DAY_29: Docstrings in Python

"""
Docstrings in Python:
Docstrings, or documentation strings, are strings that are used to document Python modules, classes, functions, and methods. They serve as documentation for the code and are accessible through the __doc__ attribute.

Usage:
Docstrings are written as the first statement in a module, function, class, or method. They provide information about the purpose, usage, parameters, and return values of the code element they document. Docstrings can be accessed using the __doc__ attribute of the respective object.

Benefits:
1. Documentation: Docstrings provide a way to document Python code, making it easier for other developers to understand and use the code.
2. Readability: Well-written docstrings improve code readability by providing clear explanations of the code's functionality.
3. Help Functionality: Docstrings can be accessed using the help() function, providing interactive documentation within the Python interpreter.

"""

# Example: Using Docstrings in Python
def square(n):
    '''This function returns the square of a number.'''
    print(n*2)

square(5)

# Accessing the docstring
print(square.__doc__)

# Zen of Python
"""
The Zen of Python, also known as PEP 20, is a collection of guiding principles for writing computer programs in Python. It emphasizes the importance of readability, simplicity, and explicitness in code. The Zen of Python can be accessed using the 'import this' statement, which prints the principles to the console.

PEP 8:
PEP 8 is the official style guide for Python code, which provides guidelines and best practices for writing clean, readable, and maintainable code. It covers topics such as naming conventions, code layout, whitespace usage, and more. Following PEP 8 ensures consistency and improves collaboration among developers.

"""

import this
