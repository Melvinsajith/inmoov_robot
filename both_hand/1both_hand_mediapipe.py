import cv2
print(cv2.__version__)
import serial
import multiprocessing as mp
import math
import HandTrackingModule as htm
import time

arduino = serial.Serial('/dev/ttyACM0',9600)

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def sendDataToArduino1(AD):
    AD = str('L'+AD).encode('UTF-8')
    arduino.write(AD)

def sendDataToArduino2(AD):
    AD = str('R'+AD).encode('UTF-8')
    arduino.write(AD)

def findPosition(self, img, handNo=0, draw=True):
    lmList = []
    if self.results.multi_hand_landmarks:
        myHand = self.results.multi_hand_landmarks[handNo]
        for id, lm in enumerate(myHand.landmark):
            # print(id, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            # print(id, cx, cy)
            lmList.append([id, cx, cy])
            if draw:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
    return lmList

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.7,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        handsType =[]
        handType =[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                # print(hand)
                # print(hand.classification)
                handType = hand.classification[0].label
                handsType.append(handType)

            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType

# width=1280
# height=720
width=640
height=480
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
detector = htm.handDetector(detectionCon=0.75)


while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))

    handData,handsType =findHands.Marks(frame)

    fingers1 = []
    fingers2 = []

    tipIds = [4,8,12,16,20]

    for hand,handType in zip(handData ,handsType):
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame,draw= False)

        if handType =="Right":
            HandColor =(255,0,0)
            print('Right')
            #print(hand)
            #print(lmList)
            if len(lmList) != 0:
        # Thumb
                if lmList[4][1] > lmList[4-1][1]:
                    print("T_open")
                    fingers1.append('1')
                else:
                    print("T_close")
                    fingers1.append('0')
                # 4 fingers
                if lmList[8][2] < lmList[8-2][2]:
                    print("I_open")
                    fingers1.append('1')

                elif lmList[8][2] > lmList[8-2][2]:
                    print("I_close")
                    fingers1.append('0')

                if lmList[12][2] < lmList[12-2][2]:
                    print("M_open")
                    fingers1.append('1')

                elif lmList[12][2] > lmList[12-2][2]:
                    print("M_close")
                    fingers1.append('0')

                if lmList[16][2] < lmList[16-2][2]:
                    print("R_open")
                    fingers1.append('1')

                elif lmList[16][2] > lmList[16-2][2]:
                    print("R_close")
                    fingers1.append('0')

                if lmList[20][2] < lmList[20-2][2]:
                    print("P_open")
                    fingers1.append('1')
                elif lmList[20][2] > lmList[20-2][2]:
                    print("P_close")   
                    fingers1.append('0')
                
            #print(fingers1)

        if handType =="Left":
            print("Left")
            #print(hand)
            HandColor =(0,0,255)
            #print(lmList)
            if len(lmList) != 0:
        
                if lmList[4][1] > lmList[4-1][1]:
                    print("T_open")
                    fingers2.append('1')
                else:
                    print("T_close")
                    fingers2.append('0')
                # 4 fingers
                if lmList[8][2] < lmList[8-2][2]:
                    print("I_open")
                    fingers2.append('1')

                elif lmList[8][2] > lmList[8-2][2]:
                    print("I_close")
                    fingers2.append('0')

                if lmList[12][2] < lmList[12-2][2]:
                    print("M_open")
                    fingers2.append('1')

                elif lmList[12][2] > lmList[12-2][2]:
                    print("M_close")
                    fingers2.append('0')

                if lmList[16][2] < lmList[16-2][2]:
                    print("R_open")
                    fingers2.append('1')

                elif lmList[16][2] > lmList[16-2][2]:
                    print("R_close")
                    fingers2.append('0')

                if lmList[20][2] < lmList[20-2][2]:
                    print("P_open")
                    fingers2.append('1')
                elif lmList[20][2] > lmList[20-2][2]:
                    print("P_close")   
                    fingers2.append('0')
            #print(fingers2)

    fingers1 = listToString(fingers1)
    print(fingers1)
    fingers2 = listToString(fingers2)
    print(fingers2)
    myArduinodata = (listToString(fingers1)) 
    print(myArduinodata)
    
    sendDataToArduino1(myArduinodata)

    myArduinodata = (listToString(fingers2)) 
    print(myArduinodata)
    
    sendDataToArduino2(myArduinodata)
        # for ind in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
        #     cv2.circle(frame,hand[ind],7,HandColor,3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
    
cam.release()