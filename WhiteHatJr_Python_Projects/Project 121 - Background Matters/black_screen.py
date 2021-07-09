import cv2
import numpy as np
# import time
# import os

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     WAITING = '\033[96m'

# def clear():
#     os.system("cls")

# def wait(x):
#     time.sleep(x)

# clear()
# print(f"{bcolors.WAITING}Loading Image")
# wait(0.25)

# clear()
# print(f"{bcolors.WAITING}Loading Image.")
# wait(0.25)

# clear()
# print(f"{bcolors.WAITING}Loading Image..")
# wait(0.25)

# clear()
# print(f"{bcolors.WAITING}Loading Image...{bcolors.ENDC}")
# wait(0.25)

#clear()
  
video = cv2.VideoCapture(0) 
image = cv2.imread("image.jpg") 
  
while True: 
  
    ret, frame = video.read() 
    print(frame)
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
  
  
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
video.release() 
cv2.destroyAllWindows() 