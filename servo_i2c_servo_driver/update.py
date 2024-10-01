import tkinter as tk
from tkinter import ttk
import time
from adafruit_servokit import ServoKit
Kit = ServoKit(channels=16)

def update_angles():
    angle1 = slider1.get()
    angle2 = slider2.get()
    angle3 = slider3.get()
    angle4 = slider4.get()
    
    # Update your application or perform actions based on the angle values
    # For demonstration, let's print the angles
    print("Angle 1: ",int(angle1))
    print("Angle 2: ",int(angle2))
    print("Angle 3: ",int(angle3))
    print("Angle 4: ",int(angle4))
    print()  # Blank line for better readability
    Kit.servo[0].angle = int(angle1)
    time.sleep(0.5)
    Kit.servo[1].angle = int(angle2)
    time.sleep(0.5)

    Kit.servo[2].angle = int(angle3)
    time.sleep(0.5)

root = tk.Tk()
root.title("Angle Control")

# Create four sliders
slider1 = ttk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300)
slider2 = ttk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300)
slider3 = ttk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300)
slider4 = ttk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, length=300)

slider1.set(0)
slider2.set(0)
slider3.set(0)
slider4.set(0)

slider1.pack()
slider2.pack()
slider3.pack()
slider4.pack()

# Create a button to update the angles
update_button = ttk.Button(root, text="Update", command=update_angles)
update_button.pack()

root.mainloop()
