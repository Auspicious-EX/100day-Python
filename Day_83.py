# DAY 83 :Exercise 9 - Shoutouts to Everyone

""" Write a program to pronounce list of names using win32 API. """


import win32com.client

def pronounce_names(names):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names:
        speaker.Speak("Shoutout to " + name)

if __name__ == "__main__":
    l = ["Rahul", "Nishant", "Harry"]
    pronounce_names(l)
