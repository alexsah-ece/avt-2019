import numpy as np
import cv2

cap = cv2.VideoCapture('Brooklyn.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #low = np.array([5, 50, 50],np.uint8)
    #high = np.array([15, 255, 255],np.uint8)
    low = np.array([10, 70, 70],np.uint8)
    high = np.array([11, 220, 220],np.uint8)
    mask = cv2.inRange(hsv,low,high)

    cv2.imshow('black',mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(33) & 0xFF:
        break
    
cap.release()
cv2.destroyAllWindows()
