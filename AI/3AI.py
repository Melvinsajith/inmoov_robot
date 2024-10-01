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
import os
import cv2
import serial
import multiprocessing as mp
import math

engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('voice','english+m1')

arduino = serial.Serial('/dev/ttyACM0',9600)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    
    print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            text = r.recognize_google(audio2)
            text = text.lower()

            print("Did you say "+text)
            #Speak(MyText)
            text = str(text)
            return text
                
def takeCommand2():
    print("Start")
    text = str(input("Tell me "))
    text = str(text)
    print("You said: " , text)
    return text

def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good       Morning!")

    elif hour >= 12 and hour <18:
        speak(" good    Afternoon!")

    elif hour > 17:
        speak("good       Evening!")

    speak("I am Humanoid robot.    Please tell me , How may I help you")


def sendDataToArduino(AD):
     
    AD = str(AD).encode('UTF-8')
    arduino.write(AD)
    
    print(AD)

def head_control(move):
    sendDataToArduino("S"+move)
    time.sleep(2)
    sendDataToArduino("T"+move)

def head_med_control(move):
    sendDataToArduino("P"+move)
    time.sleep(2)

def movement1():
    sendDataToArduino("H0")
    speak("GOOD TO SEE YOU ALL ")
    time.sleep(2)
    sendDataToArduino("H180")
    time.sleep(2)
    sendDataToArduino("H0")
    time.sleep(2)
    sendDataToArduino("G180")
    time.sleep(2)
    sendDataToArduino("G0")
    time.sleep(2)
    sendDataToArduino("I180")
    time.sleep(2)
    sendDataToArduino("I0")
    time.sleep(2)
    sendDataToArduino("J180")
    time.sleep(2)
    sendDataToArduino("J0")
    time.sleep(2)
    sendDataToArduino("K180")
    time.sleep(2)
    sendDataToArduino("K0")
    time.sleep(2)
    sendDataToArduino("M180")
    time.sleep(2)
    sendDataToArduino("M0")
    time.sleep(2)
    sendDataToArduino("N180")
    time.sleep(2)
    sendDataToArduino("N0")
    time.sleep(2)

def movement2():
    sendDataToArduino("P0")
    time.sleep(2)
    sendDataToArduino("P180")
    time.sleep(2)
    sendDataToArduino("O0")
    time.sleep(2)
    sendDataToArduino("O180")
    time.sleep(2)
    sendDataToArduino("O0")
    time.sleep(2)
    sendDataToArduino("A0")
    time.sleep(2)
    sendDataToArduino("A180")
    time.sleep(2)
    sendDataToArduino("B0")
    time.sleep(2)
    sendDataToArduino("B180")
    time.sleep(2)
    sendDataToArduino("C0")
    time.sleep(2)
    sendDataToArduino("C180")
    time.sleep(2)
    sendDataToArduino("D0")
    time.sleep(2)
    sendDataToArduino("D180")
    time.sleep(2)
    sendDataToArduino("E0")
    time.sleep(2)
    sendDataToArduino("E180")
    time.sleep(2)
    sendDataToArduino("F0")
    time.sleep(2)
    sendDataToArduino("F180")
    time.sleep(2)
wishMe()

while True:
    try:
        text = takeCommand()
    #logic for task
    except:
        print("error")
        text = " "
    
    
    if "the time" in text:
        strfTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {strfTime}")
        print(strfTime)
    
    elif "Who made you" in text:
        speak("I was made and programed by Melvin Sajith")
    
    elif "greet the audience" in text:
        speak("""Good evening, I am the first Humanoid robot built in South Africa, and my first task is to welcome you all to Africa School of Technology’s 5-year anniversary Gala Dinner.""")
        head_control("180")
        head_med_control("0")
        speak("""I believe over the past 5 years Africa School of technology has added immense value to the lives of the students who have studied there.""")
        head_control("0")
        

        speak("""It is only with the support from everyone seated here today that we can celebrate this milestone and the creation of myself, and it is only with your support can we as Africa School of Technology move forward and achieve more groundbreaking strides whiles changing the lives of students. """)
        head_control("180")
        head_med_control("180")

        speak("""The Team at Africa School of Technology thanks you for being a part of this, and we hope you enjoy your night with us as we celebrate the last 5-years.""")
        head_control("0")
        head_med_control("90")
    
    
    elif "movement 1" in text:
        movement1()
    elif "movement 2" in text:
        movement2()