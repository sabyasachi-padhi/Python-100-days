#in day 83 we are doing another excersize called shout out to everyone...
#we are using win32 API.......

import pyttsx3

shoutout=["tarinee" , "harry", "love" , "kunal" ,"miku"  ,"tiku" ]

engine=pyttsx3.init()

for name in shoutout:
    engine.say(f"shoutout to {name}")
    engine.runAndWait()
