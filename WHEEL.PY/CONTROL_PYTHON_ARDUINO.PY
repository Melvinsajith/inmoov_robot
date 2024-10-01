
import serial 
import time
arduinoData = serial.Serial('/dev/ttyACM0',9600)

while True:
    time.sleep(0.5)
    #mydata = "melvin"
    #mydata = input("Enter 1 or 0") 
    mydata = input("enter data")
    if mydata == 'q':
        break
    mydata = str(mydata).encode('UTF-8')
    print(mydata)
    arduinoData.write(mydata)
    time.sleep(1)
    