from adafruit_servokit import ServoKit
import time

Kit = ServoKit(channels=16)
Kit.servo[0].angle = 90
time.sleep(2)

Kit.servo[0].angle = 180
time.sleep(2)

Kit.servo[2].angle = 180
time.sleep(2)
Kit.servo[2].angle = 90
