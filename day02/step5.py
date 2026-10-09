import cv2
import numpy as np

img = cv2.imread("images/02_colour_bars.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([50, 100, 100])
upper = np.array([70, 255, 255])

mask = cv2.inRange(hsv,lower,upper)
result = cv2.bitwise_and(img,img,mask=mask)

print("mask shape        :", mask.shape)
print("mask at green bar :", mask[100, 350])
print("mask at red bar   :", mask[100, 550])
print("white pixels      :", np.count_nonzero(mask))

cv2.imshow("original", img)
cv2.imshow("mask", mask)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()