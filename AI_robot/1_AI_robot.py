import os
import cv2
import time
import pyttsx3
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

def sendDataToArduino(AD):
     
    AD = str(AD).encode('UTF-8')
    arduino.write(AD)
    
    print(AD)

def head_control(move):
    sendDataToArduino("G"+move)
    time.sleep(2)

    sendDataToArduino("H"+move)
    time.sleep(2)

    


speak("""Good evening, I am the first Humanoid robot built in South Africa, and my first task is to welcome you all to Africa School of Technology’s 5-year anniversary Gala Dinner.""")
head_control("180")

speak("""I believe over the past 5 years Africa School of technology has added immense value to the lives of the students who have studied there.""")
head_control("0")

speak("""It is only with the support from everyone seated here today that we can celebrate this milestone and the creation of myself, and it is only with your support can we as Africa School of Technology move forward and achieve more groundbreaking strides whiles changing the lives of students. """)
head_control("180")

speak("""The Team at Africa School of Technology thanks you for being a part of this, and we hope you enjoy your night with us as we celebrate the last 5-years.""")
head_control("0")

while True:

    head_control("180")
    head_control("0")
