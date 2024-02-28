# DAY 94 : Exercise 11 - Drink Water Reminder 

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

# (1)
# import time
# import winsound

# def drink_water_reminder():
#     sound_file = "path/to/sound.wav"  # Replace with the path to your sound file
#     sound_duration = 500  # Duration of the sound in milliseconds

#     while True:
#         # Play the sound
#         winsound.PlaySound(sound_file, winsound.SND_FILENAME)
#         print("Pani pi lo yaar, zaroori hai. Main phir ek ghante baad milta hoon!")
#         # Wait for an hour (3600 seconds) before the next reminder
#         time.sleep(15)

# if __name__ == "__main__":
#     drink_water_reminder()

# (2)
# import time
# import winsound
# import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def drink_water_reminder():
#     reminder_message = "Drink water buddy, it's important. I'll remind you again in one hour."

#     while True:
#         speak(reminder_message)
#         # Beep sound
#         winsound.Beep(1000, 500)  # Frequency = 1000Hz, Duration = 500ms
#         # Wait for an hour (3600 seconds) before the next reminder
#         time.sleep(15)

# if __name__ == "__main__":
#     drink_water_reminder()