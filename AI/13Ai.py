
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
engine.setProperty('voice','english+m2')

arduino = serial.Serial('COM6',9600)
#arduino2 = serial.Serial('COM7',9600)


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



def sendDataToArduino(AD):
     
    AD = str(AD).encode('UTF-8')
    arduino.write(AD)
    time.sleep(3)
    
    print(AD)

def sendDataToArduino2(AD):
     
    AD = str(AD).encode('UTF-8')
    arduino2.write(AD)
    time.sleep(2)

    print(AD)





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
    sendDataToArduino2("L11111")
    time.sleep(2)
    sendDataToArduino2("R11111")

    sendDataToArduino("J180")
    time.sleep(2)
    sendDataToArduino("J0")
    time.sleep(2)
    sendDataToArduino2("L00000")
    time.sleep(2)
    sendDataToArduino2("R00000")

    sendDataToArduino("K180")
    time.sleep(2)
    sendDataToArduino("K0")
    time.sleep(2)
    sendDataToArduino("M180")
    time.sleep(2)
    sendDataToArduino("M0")
    time.sleep(2)
    




def movement3():
    
    sendDataToArduino("D180")
    time.sleep(2)
    sendDataToArduino("D0")
    time.sleep(2)
    sendDataToArduino("C180")
    time.sleep(2)
    sendDataToArduino("C0")
    time.sleep(2)
    sendDataToArduino("D180")
    sendDataToArduino("C180")
    time.sleep(2)
    sendDataToArduino("D0")
    sendDataToArduino("C0")

    



wishMe()
speak("I am a Humanoid robot.    Please tell me , How may I help you")

while True:
    try:
        text = takeCommand()
    #logic for task
    except:
        print("error")
        speak("it was not clear can you repeat again ")
        text = " "
    
    if "wikipedia" in text:
        text = text.replace("wikipedia" , " ")
        try:
            result = wikipedia.summary(text , sentences = 1)
            speak("According to wikipedia")
            sendDataToArduino("T90")

            print(result)
            speak(result)
        except:
            print("next")

    if "the time" in text:
        strfTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {strfTime}")
        print(strfTime)

    if "lift arm" in text:
        sendDataToArduino("U")

    if "right arm" in text:
        sendDataToArduino("V")