import cv2
<<<<<<< ba28e1e0e5c0e16b1ec551fd018be3b7f8eb792a
import numpy as np
def nothing(a):
    pass
cap = cv2.VideoCapture('youth.mp4') # video input 
cv2.namedWindow('black') # create new window 
img = cv2.imread('screen.jpg',1) # image input 
dim = (500, 500) # choose dimensions 
img = cv2.resize(img, dim) # create trackbar 
#trackbar for low values 
cv2.createTrackbar('RL','black',0,255,nothing)
cv2.createTrackbar('GL','black',0,255,nothing)
cv2.createTrackbar('BL','black',0,255,nothing)
#trackbar for high values 
cv2.createTrackbar('RH','black',0,255,nothing)
cv2.createTrackbar('GH','black',0,255,nothing)
cv2.createTrackbar('BH','black',0,255,nothing)
=======

cap = cv2.VideoCapture('steph.mp4') # open the video 
>>>>>>> Add 27 character for escape

while(cap.isOpened()):
    ret, frame = cap.read() # read each video's frame 

<<<<<<< ba28e1e0e5c0e16b1ec551fd018be3b7f8eb792a
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # get trackbar values
    rl = cv2.getTrackbarPos('RL','black')  
    gl = cv2.getTrackbarPos('GL','black')
    bl = cv2.getTrackbarPos('BL','black')
    
    rh = cv2.getTrackbarPos('RH','black')
    gh = cv2.getTrackbarPos('GH','black')
    bh = cv2.getTrackbarPos('BH','black')
    
    low = (rl, gl, bl)
    high = (rh, gh, bh)
    mask = cv2.inRange(hsv,low,high) # apply values in our mask 
    
    cv2.imshow('black',mask)
    cv2.imshow('image',img)
    #cv2.imshow('frame',frame)
    if cv2.waitKey(33) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
=======
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # change colour's scale from BGR to HSV 
    low = np.array([5, 50, 50],np.uint8) # initial low values 
    high = np.array([15, 255, 255],np.uint8) # initial high values 
    #low = np.array([8, 93, 98],np.uint8) # modified values  
    #high = np.array([15, 253, 223],np.uint8) # modified values 
    mask = cv2.inRange(hsv,low,high) # apply a mask in each frame in order to isolate the colours that we are interested in 

    cv2.imshow('black',mask) # show mask 
    cv2.imshow('frame',frame) # show original image 
    if cv2.waitKey(33) & 0xFF == 27: # exit when button esc is pressed 
        break
    
cap.release() # release video 
cv2.destroyAllWindows() # close windows 
>>>>>>> Add 27 character for escape
