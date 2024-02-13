# DAY_19: break and continue in Python and Do While loop

""" 
The 'break' and 'continue' statements are control flow statements used in loops.

- 'break' statement: Terminates the loop it is in and transfers the execution to the statement immediately following the loop.

- 'continue' statement: Skips the rest of the code inside a loop for the current iteration and jumps to the next iteration.

"""

# Example 1: Using 'break' in a for loop
for i in range(1, 10):
    print(" 5 X", i, "=", 5*i)
    if i == 8:
        break
print("Whole loop is broken")

# Example 2: Using 'continue' in a for loop
for i in range(1, 10):
    if i == 8:
        print("Skip iteration")
        continue
    print(" 5 X", i, "=", 5*i)

# Do-While loop emulation
# In Python, there's no direct 'do-while' loop, but you can emulate its behavior using a 'while' loop.

""" 
Do-While loop:
A loop that executes a block of code at least once, and then repeats as long as a certain condition is true.
"""

i = 0
while True:
    print(i)
    i += 1
    if i % 100 == 0:
        break
