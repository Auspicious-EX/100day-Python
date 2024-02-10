#Day_15: Exercise: WAP which Great based on timesatemp

import time

timestamp = int(time.strftime('%H'))
print(timestamp)

if 4 <= timestamp < 12:
    print("Good Morning")
elif 12 <= timestamp < 16:
    print("Good Afternoon")
elif 16 <= timestamp < 21:
    print("Good Evening")
else:
    print("Good Night")
