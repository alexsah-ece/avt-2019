import cv2
import numpy as np
cap = cv2.VideoCapture('steph.mp4')

cv2.createTrackbar('R','black',0,255,nothing)
cv2.createTrackbar('G','black',0,255,nothing)
cv2.createTrackbar('B','black',0,255,nothing)


while(cap.isOpened()):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #low = np.array([5, 50, 50],np.uint8)
    #high = np.array([15, 255, 255],np.uint8)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,400)
    low = (5, 50, 50)
    high = (15, 255, 255)
    mask = cv2.inRange(hsv,low,high)
    if circles is not None:
        circles = np.round(circles[0,:]).astype("int")
        for (x, y, r) in circles:
            if mask[y,x] != 0:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
                
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')

    cv2.imshow('black',mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
