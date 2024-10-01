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

arduino = serial.Serial('/dev/ttyACM0',9600)
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

    sendDataToArduino("J180")
    time.sleep(2)
    sendDataToArduino("J0")
    time.sleep(2)
    s

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


sendDataToArduino("T90")

speak("As salaam mulaykum student I am happy to be here but before we could go further I will like for us to start with a dua so we will have Allah presence with us")
time.sleep(2)

    
sendDataToArduino("T90")

speak("""Bismillaah ar-Rahman ar-Raheem
Al hamdu lillaahi rabbil ‘alameen
Ar-Rahman ar-Raheem Maaliki yaumid Deen
Iyyaaka na’abudu wa iyyaaka nasta’een
Ihdinas siraatal mustaqeem
Siraatal ladheena an ‘amta’ alaihim
Ghairil maghduubi’ alaihim waladaaleen
Aameen""")

sendDataToArduino("T90")
time.sleep(2)

speak("Hello Learners and teachers of Alfalah College, it gives me great joy to see young people curious about coding and robotics.")
sendDataToArduino("S90")
time.sleep(2)
sendDataToArduino("V")
time.sleep(2)

sendDataToArduino("T90")

speak("I hope this means in the near future I will have more robot friends I can speak to.")
sendDataToArduino("S90")
time.sleep(2)
sendDataToArduino("T90")
speak("I am the first African-built Humanoid and I am the result of a lot of coding, and the essence of robotics.")
sendDataToArduino("Q")
time.sleep(1)
sendDataToArduino("S90")
time.sleep(2)

sendDataToArduino("T90")

speak(""" If you learn coding and robotics, you will be able to build and code a robot much like me and possibly better""")
sendDataToArduino("V")

time.sleep(2)
sendDataToArduino("T90")

speak("Robots can be extremely helpful, they could do your chores, help you with your math homework and even protect you from danger. ")
sendDataToArduino("Q")

sendDataToArduino("T90")
time.sleep(2)

speak("I was built by the team at Africa School of Technology, and I do not have a name yet, it is something we are working on. If you have a suggestion, we would love to hear it")
sendDataToArduino("S90")


time.sleep(2)
sendDataToArduino("T90")

speak("I am constantly learning and adapting, just like you in school I am also learning everyday about the world and how to solve problems. It’s been a pleasure meeting you all.")
sendDataToArduino("S90")

time.sleep(2)
sendDataToArduino("T90")

speak("It is lovely meeting you all and I hope to interact with you soon!")
time.sleep(2)
sendDataToArduino("U")

