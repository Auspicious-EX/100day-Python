# DAY-14 : If Else Conditional Statements in Python

# if-else Statements: Conditional execution based on a condition.

# Takes user input for age.
a = int(input("Enter your age: "))
print("Your age is", a)

# Conditional Operators: >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if-else statement: Executes one block of code if a condition is true, another if false.
if a > 18:
    print("You can drive")
    print("yes")
else:
    print("You cannot drive")
    print("NO")

# elif statement: Allows checking multiple conditions.
num = int(input("Enter the value of num: "))
if num < 0:
    print("Number is negative.")
elif num == 0:
    print("Number is Zero.")
elif num == 999:
    print("Number is Special.")
else:
    print("Number is positive.")

print("I am happy now")

# Nested if: if statement inside another if statement.
num = 18
if num < 0:
    print("Number is negative.")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif 10 < num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
