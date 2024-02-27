# DAY 88 :Exercise 9: Solution - Shoutouts to Everyone

import win32com.client

def pronounce_names(names):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names:
        speaker.Speak("Shoutout to " + name)

if __name__ == "__main__":
    l = ["Rahul", "Nishant", "Harry"]
    pronounce_names(l)