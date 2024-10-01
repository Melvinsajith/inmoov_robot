import serial 
import time
arduinoData = serial.Serial('/dev/ttyACM0',9600)

while True:
    time.sleep(0.5)
    mydata = "melvin"
    #a = input("Enter 1 or 0") 
    mydata = input("enter data")
    if mydata == 'q':
        break
    mydata = str(mydata).encode('UTF-8')
    print(mydata)
    arduinoData.write(mydata)
    time.sleep(2)
    right_elbow_angle = "90"
    right_elbow_angle = "G" + right_elbow_angle + '\r'
    right_elbow_angle = str(right_elbow_angle).encode('UTF-8')
    print(right_elbow_angle)
    arduinoData.write(right_elbow_angle)
