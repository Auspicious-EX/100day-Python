# DAY_41: Short hand if-else statements

""" 
If ... Else in One Line:
There is a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short.

Syntax:
result = value_if_true if condition else value_if_false

Equivalent to:
if condition:
    result = value_if_true
else:
    result = value_if_false

Conclusion:
The shorthand syntax can be convenient for writing simple if-else statements, especially for assigning a value to a variable based on a condition. However, it's not suitable for complex situations requiring multiple statements or more complex logic.
In such cases, it's best to use the full if-else syntax.
 """

a = 300
b = 3000
print("A") if a > b else print("=") if a == b else print("B")

c = 10 if a > 30 else print("No")

print(c)
