# DAY 99 : Exercise 11: Solution + Shoutouts - Desktop Notification System

"""  
Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system
"""

import time
from plyer import notification

def drink_water_reminder():
    notification_title = "Drink Water Reminder"
    notification_message = "Pani pi lo yaar, zaroori hai. Main phir ek ghante baad milta hoon!"
    notification_timeout = 10  # Notification timeout in seconds

    while True:
        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=notification_timeout
        )
        # Wait for an hour (3600 seconds) before the next reminder
        time.sleep(15)

if __name__ == "__main__":
    drink_water_reminder()