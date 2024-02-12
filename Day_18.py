# Day_18: While Loops in Python

""" 
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter exits the while loop.
"""

# Example 1: Simple while loop
i = 0
while i < 3:
    print(i)
    i += 1

print("Done")

# Example 2: While loop with user input
# Uncomment and fix the commented code to work properly
# i = int(input("Enter the number: "))
# while i < 3:
#     i = int(input("Enter the number: "))
#     print(i)
#     i += 1
# print("Done")

"""  
Else with While Loop
We can even use the else statement with the while loop. 
Essentially, when the while loop condition becomes False, the interpreter exits the while loop, and the else statement is executed.
"""

# Example 3: While loop with else
x = 5
while x > 0:
    print(x)
    x -= 1
else:
    print('Counter is 0')

# Emulating do-while loop behavior
# In Python, there's no direct equivalent of the do-while loop, but we can achieve similar behavior using a while loop.

# do {
#     // code
# } while(condition)

# Emulating the same behavior in Python:
# This code will execute at least once before checking the condition.
# Uncomment and fix the commented code to work properly
# while True:
#     # code
#     if not condition:
#         break
