from adafruit_servokit import ServoKit
import time 

mykit = ServoKit(channels=16)

mykit.servo[0].angle= 90
time.sleep(2)
mykit.servo[0].angle= 0
