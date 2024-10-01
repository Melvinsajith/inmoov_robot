import os
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate',100)

engine.setProperty('voice','english+m2')

text = " how are you , what would you like me to Speak"

engine.say(text)

engine.runAndWait()

while True:
    a = str(input ("enter what to say"))
    engine.say(a)
    engine.runAndWait()


