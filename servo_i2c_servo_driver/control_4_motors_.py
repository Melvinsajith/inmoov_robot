import tkinter as tk
import serial 
import time
from adafruit_servokit import ServoKit
Kit = ServoKit(channels=16)

def update_angles(slider_num, value):
    # Update your application or perform actions based on the angle values
    # For demonstration, let's print the angle values
    angles[slider_num] = value
    print(f"Angle 1: {angles[0]}")
    print(f"Angle 2: {angles[1]}")
    print(f"Angle 3: {angles[2]}")
    print(f"Angle 4: {angles[3]}")
    print()  # Blank line for better readability
    print("angles = ", angles)
    

    Kit.servo[0].angle = int(angles[0])
    Kit.servo[1].angle = int(angles[1])
    Kit.servo[2].angle = int(angles[2])
    Kit.servo[3].angle = int(angles[3])



root = tk.Tk()
root.title("Angle Control")

# Initialize angle values
angles = [0, 0, 0, 0]

# Create four sliders
slider1 = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda value: update_angles(0, value))
slider2 = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda value: update_angles(1, value))
slider3 = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda value: update_angles(2, value))
slider4 = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda value: update_angles(3, value))

slider1.set(0)
slider2.set(0)
slider3.set(0)
slider4.set(0)

slider1.pack()
slider2.pack()
slider3.pack()
slider4.pack()


root.mainloop()

