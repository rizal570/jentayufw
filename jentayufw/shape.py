import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.rectangle(img, (0,0),(250,350),(213,123,23),2)
cv2.putText(img, "Toilet", (300,100), cv2.FONT_HERSHEY_COMPLEX,3,(0,213,51),1)


cv2.imshow("Output", img)
cv2.waitKey(0)