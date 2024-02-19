# DAY_38: Raising custom errors in Python

# Asking user to enter a value between 5 and 9
a = int(input("Enter any value between 5 and 9: "))

# Checking if the entered value is within the specified range
if a < 5 or a > 9:
    raise ValueError("Value must be between 5 and 9")

""" 
Raising Custom Errors:
In Python, custom errors can be raised using the raise keyword.
 """

# Asking user to enter a salary amount
salary = int(input("Enter salary amount: "))

# Checking if the salary is within a valid range
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

""" 
Defining Custom Exceptions:
In Python, custom exceptions can be defined by creating a new class derived from the built-in Exception class.

Syntax:
class CustomError(Exception):
    # Define custom properties and methods
    pass

try:
    # Code that could potentially raise the custom error
except CustomError:
    # Handling code for the custom error
 """

# Example:
class SalaryOutOfRangeError(Exception):
    """Exception raised for salaries out of the valid range."""
    pass

try:
    # Code that could potentially raise the custom error
    salary = int(input("Enter salary amount: "))

    # Checking if the salary is within a valid range
    if not 2000 < salary < 5000:
        raise SalaryOutOfRangeError("Salary must be between 2000 and 5000.")

except SalaryOutOfRangeError as e:
    # Handling code for the custom error
    print(e)

#Example:
# Asking user to enter a value or "quit" to exit
value = input("Enter any value or 'quit' to exit: ")

# Checking if the user wants to exit
if value.lower() == 'quit':
    print("Exiting program...")
else:
    try:
        # Converting user input to integer
        a = int(value)

        # Checking if the entered value is within the specified range
        if a < 5 or a > 9:
            raise ValueError("Value must be between 5 and 9")

        print("Value is within the specified range.")

    except ValueError as e:
        # Handling code for invalid input
        print("Invalid input:", e)
