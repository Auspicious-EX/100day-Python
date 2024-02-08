#DAY 10 : Taking User Input in Python

print( 
"""

Taking User Input in Python:
    - In python, we can take user input by using the input() function.
    - The input() function is used to take input from the user.
    - The input() function always returns a string value.
    - Syntax:
        - variable_name = input("Enter your message here")
    - Example:
        - name = input("Enter your name: ")
        - print("Hello", name)
        - print(type(name))
""")

print("\nArithmatic Calclulater using user imput")

a = float(input("\nEnter the first Number: "))
b = float(input("\nEnter the second Number: "))

print("the sum of {a} and {b}:", a + b)
print("the difference of {a} and {b}:", a - b)
print("the product of {a} and {b}:", a * b)
print("the division of {a} and {b}:", a / b)
print("the remainder of {a} and {b}:", a % b)
print("the power of {a} and {b}:", a ** b)

