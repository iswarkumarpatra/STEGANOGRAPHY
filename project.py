import cv2
import numpy as np
import os

image_path = r"C:\Users\iswar\Desktop\cyber security\s.png"

img = cv2.imread(image_path)

# Check if the image was loaded correctly
if img is None:
    print("Error: Image not found or could not be read. Check the file path.")
    exit()

# Convert image to an editable format (8-bit BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR) if img.shape[-1] == 4 else img

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

n, m, z = 0, 0, 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]  # Keep n within image height
    m = (m + 1) % img.shape[1]  # Keep m within image width
    z = (z + 1) % 3  # Cycle through RGB channels

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open image in default viewer (Windows)

message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]  
        m = (m + 1) % img.shape[1]  
        z = (z + 1) % 3  
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
