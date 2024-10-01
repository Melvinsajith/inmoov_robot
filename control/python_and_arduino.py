import serial

arduinodata = serial.Serial('/dev/ttyACM0',9600)

while True:
    data1 = input('Please Enter your command')
    
    data1 = data1+'\r'
    arduinodata.write(data1.encode())

    right_elbow_angle = "0"
    right_elbow_angle = "1" + right_elbow_angle + '\r'
    right_elbow_angle = str(right_elbow_angle).encode()
    print(right_elbow_angle)
    arduinodata.write(right_elbow_angle)