import cv2
import numpy as np

def empty(a):
    pass

path = "circles.png"

cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars",(640,240))
cv2.createTrackbar("Hue Min", "Track Bars", 34, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 55, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 160, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv2.createTrackbar("Value Min", "Track Bars", 34, 255, empty)
cv2.createTrackbar("Value Max", "Track Bars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    hmin = cv2.getTrackbarPos("Hue Min","Track Bars")
    hmax = cv2.getTrackbarPos("Hue Max", "Track Bars")
    smin = cv2.getTrackbarPos("Sat Min", "Track Bars")
    smax = cv2.getTrackbarPos("Sat Max", "Track Bars")
    vmin = cv2.getTrackbarPos("Value Min", "Track Bars")
    vmax = cv2.getTrackbarPos("Value Max", "Track Bars")
    
    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original Image", img)
    cv2.imshow("HSV Image", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Final Output", imgResult)
    cv2.waitKey(1)