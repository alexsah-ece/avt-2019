import cv2
import numpy as np
def nothing(a):
    pass
cap = cv2.VideoCapture('steph.mp4')
cv2.namedWindow('black')
img = cv2.imread('screen2.png',1)
dim = (500, 500)
img = cv2.resize(img, dim) 
cv2.createTrackbar('RL','black',0,255,nothing)
cv2.createTrackbar('GL','black',0,255,nothing)
cv2.createTrackbar('BL','black',0,255,nothing)

cv2.createTrackbar('RH','black',0,255,nothing)
cv2.createTrackbar('GH','black',0,255,nothing)
cv2.createTrackbar('BH','black',0,255,nothing)

while(cap.isOpened()):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   
    #low = np.array([5, 50, 50],np.uint8)
    #high = np.array([15, 255, 255],np.uint8)
    
    rl = cv2.getTrackbarPos('RL','black')
    gl = cv2.getTrackbarPos('GL','black')
    bl = cv2.getTrackbarPos('BL','black')
    
    rh = cv2.getTrackbarPos('RH','black')
    gh = cv2.getTrackbarPos('GH','black')
    bh = cv2.getTrackbarPos('BH','black')
    
    low = (rl, gl, bl)
    high = (rh, gh, bh)
    mask = cv2.inRange(hsv,low,high)
    
                

    cv2.imshow('black',mask)
    cv2.imshow('image',img)
    #cv2.imshow('frame',frame)
    if cv2.waitKey(70) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
