# DAY 84 :Time Module in Python
import time

""" 
The time Module in Python
The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the time module in Python and see how it can be used in different scenarios.
 """

""" 
time.time()
The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time. Here's an example:

import time
 """
def usingwhile():
    i = 0
    while i < 500:
        i = i+1
        print(i)

def usingFor():
    for i in range(500):
        print(i)

init= time.time()
usingFor()
t1 = time.time() - init
init= time.time()
usingwhile()
print(t1)
print(time.time() - init)

""" 
time.sleep()
The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads. Here's an example:
 """

print(4)
time.sleep(3)
print("This is  printed after 3 seconds")


""" 
time.strftime()
The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report. Here's an example:
As you can see, the function time.strftime() formats the current time (obtained using time.localtime()) as a string, using a specified format. The format string contains codes that represent different parts of the time value, such as the year, the month, the day, the hour, the minute, and the second.
 
 """
import time

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
# Output: 2022-11-08 08:45:33


""" 
Conclusion
The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. Whether you are writing a script, a library, or an application, the time module is a powerful tool that can help you perform time-related tasks with ease and efficiency. So, if you haven't already, be sure to check out the time module in Python and see how it can help you write better, more efficient code.
 """