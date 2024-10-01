import tkinter as tk
import cv2

def capture_photo():
    camera = cv2.VideoCapture(0)  # Open the camera
    _, image = camera.read()  # Read an image from the camera

    cv2.imwrite("captured_photo.png", image)  # Save the captured photo as "captured_photo.png"

    camera.release()  # Release the camera

def convert_to_black_and_white():
    image = cv2.imread("captured_photo.png")  # Read the captured photo
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

    cv2.imwrite("black_and_white_photo.png", gray_image)  # Save the black and white photo as "black_and_white_photo.png"

    cv2.imshow("Black and White Photo", gray_image)  # Display the black and white photo
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows

def close_program():
    window.destroy() 


window = tk.Tk()
window.title("Photo App")

capture_button = tk.Button(window, text="Capture Photo", command=capture_photo)
capture_button.pack(pady=10)

convert_button = tk.Button(window, text="Convert to Black and White", command=convert_to_black_and_white)
convert_button.pack(pady=10)

window.protocol("WM_DELETE_WINDOW", close_program)


window.mainloop()
