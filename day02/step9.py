import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread("images/02_colour_bars.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("controls")
cv2.createTrackbar("H low", "controls", 50, 179, nothing)
cv2.createTrackbar("H high", "controls", 70, 179, nothing)
cv2.createTrackbar("S low", "controls", 100, 255, nothing)
cv2.createTrackbar("V low", "controls", 100, 255, nothing)

while True:
    h_low = cv2.getTrackbarPos("H low", "controls")
    h_high = cv2.getTrackbarPos("H high", "controls")
    s_low = cv2.getTrackbarPos("S low", "controls")
    v_low = cv2.getTrackbarPos("V low", "controls")

    lower = np.array([h_low, s_low, v_low])
    upper = np.array([h_high, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()