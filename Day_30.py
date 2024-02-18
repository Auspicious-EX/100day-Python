# DAY_30: Recursion in Python

"""
Recursion in Python:
Recursion is the process of defining something in terms of itself. In programming, recursion involves a function calling itself to solve smaller instances of a problem. Recursive functions break down a problem into smaller, more manageable subproblems until a base case is reached.

Python Recursive Function:
In Python, functions can call other functions, including themselves. These recursive functions allow for elegant solutions to problems that can be broken down into simpler cases. However, recursive functions must have a base case to prevent infinite recursion.

"""

#factorial(7) = 7*6*5*4*3*2*1
#factorial(0) = 1

#factorial(n)= n * factorial(n-1)

# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))

# Example: Fibonacci Sequence using Recursion
def fibonacci(n):
    """Returns the Fibonacci sequence up to the nth term."""
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence

# Generate Fibonacci sequence up to the 9th term
fib_sequence = fibonacci(9)
print(fib_sequence)
