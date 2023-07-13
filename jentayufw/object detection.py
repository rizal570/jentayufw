import cv2
import numpy as np

path = "circles.png"
img = cv2.imread(path)

imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur,100,100)

contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for cnt in contours:
        area = cv2.contourArea(cnt)
        print("area: " + str(area))
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
            para = cv2.arcLength(cnt,True)
            print("perimeter: " + str(para))
            approx = cv2.approxPolyDP(cnt,0.02*para,True)
            print("approximate points: " + str(len(approx)))

cv2.imshow("Contour Detection",imgContour)
cv2.waitKey(0)