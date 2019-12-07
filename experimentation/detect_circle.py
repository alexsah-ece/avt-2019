import cv2
import numpy as np


img = cv2.imread('/home/alex/Desktop/tennis_ball.png')

# img = cv2.imread('/home/alex/Desktop/nba2k.png')
cv2.imshow('blurred',img)
img = cv2.medianBlur(img,5)

greenLower = (14, 155, 76)
greenUpper = (45, 255, 255)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, greenLower, greenUpper)
cv2.imshow('blurred',mask)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

cv2.imshow('blurred',mask)

kernel = np.ones((5,5),np.uint8)
ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, ellipse)

cv2.imshow('gradient',gradient)

im2, contours, hierarchy = cv2.findContours(gradient.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im2, contours, -1, (0,255,255), 3)
cv2.imshow('contours',im2)

# cimg = cv2.cvtColor(mask,cv2.COLOR_HSV2BGR)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('blurred',cimg)


circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1, 100,
                            param1=50,param2=30,minRadius=20,maxRadius=100)

print(circles)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()