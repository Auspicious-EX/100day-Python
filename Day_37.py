# DAY_37: Finally keyword in Python

""" 
Finally Clause:
The finally code block is a part of exception handling. It is always executed, whether an exception is raised or not. It's generally used for concluding tasks like closing file resources, database connections, or ending the program execution with a message.

Syntax:
try:
    # Code that could potentially raise an exception
except:
    # Handling code for the exception
finally:
    # Code that is always executed, regardless of whether an exception occurred or not
 """

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the Index: "))
        print(l[i])
        return 1

    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed")
    # print("I am always executed")

x = func1()
print(x)
