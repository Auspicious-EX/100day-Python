# DAY_35: for Loop with else in Python

"""
Python - else in Loop:
Python allows the else keyword to be used with the for and while loops. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

Syntax:
for counter in sequence:
    # Statements inside for loop block
else:
    # Statements inside else block
"""

# Example 1: while loop with else
i = 0
while i < 7:
    print(i)
    i += 1
else:
    print("The while loop is completed.")

# Example 2: for loop with else
for i in range(5):
    print("hello", i)
else:
    print("The for loop is completed.")

# Example 3: for loop with break statement
for i in range(7):
    print("hello", i)
    if i == 4:
        break
else:
    print("The for loop is completed without encountering a break.")
# In Example 3, when the value of i becomes 4, the break statement is encountered, which terminates the loop prematurely. As a result, the else block is not executed, indicating that the loop was not completed without a break.
