import cv2
import time
import os
import HandTrackingModule as htm
import serial
import multiprocessing as mp
import math

dispW  =640
dispH= 480
arduino = serial.Serial('/dev/ttyACM0',9600)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
def sendDataToArduino(AD):
     
    AD = str(AD).encode('UTF-8')
    arduino.write(AD)
    
    print(AD)
    time.sleep(2)
    


Ptime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4,8,12,16,20]

while True:
    sucees , img = cap.read()
    #time.sleep(0.2)

    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw= False)
    #print(lmList)
    fingers = []

    if len(lmList) != 0:
        # Thumb
        if lmList[4][1] > lmList[4-1][1]:
            print("T_open")
            fingers.append('1')
        else:
            print("T_close")
            fingers.append('0')
        # 4 fingers
        if lmList[8][2] < lmList[8-2][2]:
            print("I_open")
            fingers.append('1')

        elif lmList[8][2] > lmList[8-2][2]:
            print("I_close")
            fingers.append('0')

        if lmList[12][2] < lmList[12-2][2]:
            print("M_open")
            fingers.append('1')

        elif lmList[12][2] > lmList[12-2][2]:
            print("M_close")
            fingers.append('0')

        if lmList[16][2] < lmList[16-2][2]:
            print("R_open")
            fingers.append('1')

        elif lmList[16][2] > lmList[16-2][2]:
            print("R_close")
            fingers.append('0')

        if lmList[20][2] < lmList[20-2][2]:
            print("P_open")
            fingers.append('1')
        elif lmList[20][2] > lmList[20-2][2]:
            print("P_close")   
            fingers.append('0')

    totalFingers = fingers.count('1')
    print(totalFingers)

    cv2.putText(img,f'{totalFingers}',(100,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),3)



    cTime = time.time()
    fps =1/(cTime-Ptime)
    Ptime = cTime 

    cv2.putText(img,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),3)

    cv2.imshow("image",img)
    #cv2.moveWindow('Image',0,0)
    print(fingers)
    myarduinodata = (listToString(fingers))
    #sendDataToArduino(myArduinodata)
    p1 =mp.Process(target=sendDataToArduino ,args = {myarduinodata})
    
    p1.start()

    

    if cv2.waitKey(1)==ord('q'):
        break
cap.release() 
    
cv2.destroyAllWindows()   
exit()
