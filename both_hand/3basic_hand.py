from pprint import pprint
import cv2 
import mediapipe as mp
import time
width=640
height=480

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

mpDraw = mp.solutions.drawing_utils


class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
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


findHands=mpHands(2)

while True:
    success , img = cap.read()

    imgRGB = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        handData,handsType =findHands.Marks(imgRGB)
    for hands,handType in zip(handData ,handsType):
        if handType =="Right":
            HandColor =(255,0,0)
            print(handData)
            time.sleep(1)
        if handType =="Left":
            HandColor =(0,0,255)
            print(handData)
            print("Left")
    
            #print(handlms)
    
   
    cv2.imshow("image",img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
