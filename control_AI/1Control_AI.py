from distutils.command.build import build
import os
from time import strftime
from tkinter.filedialog import Open
from typing import Text
import webbrowser
from cupshelpers import Device
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import webbrowser
import urllib.request 
import time
import time
import serial

dispW  =640
dispH= 480
arduino = serial.Serial('/dev/ttyACM0',9600)

engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('voice','english+m1')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone(device_index = 9) as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(" User Said:" , query )
    except Exception as e:
        print("Say that agin please...")
        return "None"
    return query

def takeCommand2():
    print("Start")
    text = str(input("Tell me "))
    text = str(text)
    print("You said: " , text)
    return text

def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good Morning!")

    elif hour >= 12 and hour <18:
        speak("good Afternoon!")

    elif hour > 17:
        speak("good Evening!")
    speak("I am Max Sir. Please tell me , How may I help you")

#speak("Melvin is a good boy")

def sendDataToArduino(AD):
    AD = str(AD).encode('UTF-8')
    arduino.write(AD)

def webopen(Url):
    Open1 = urllib.request.urlopen(Url)  

wishMe()
while True:
    text = takeCommand2()
    #logic for task
    if 'wikipedia' in text:
        speak('Searching Wikipedia...')
        text = text.replace('wikipedia'," ")
        results = wikipedia.summary(text, sentences = 2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    
    
    elif "the time" in text:
        strfTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {strfTime}")
        print(strfTime)
    
    elif "Who made you" in text:
        speak("I was made and programed by Melvin Sajith")

    
    elif "open Right arm" in text:
        myarduinodata = "R11111"
        sendDataToArduino(myarduinodata)
    
    elif "open Left arm" in text:
        myarduinodata = "L11111"
        sendDataToArduino(myarduinodata)
    
    elif "close right arm" in text:
        myarduinodata = "R00000"
        sendDataToArduino(myarduinodata)
    
    elif "close left arm" in text:
        myarduinodata = "L00000"
        sendDataToArduino(myarduinodata)   