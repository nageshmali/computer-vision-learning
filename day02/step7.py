import cv2
import numpy as np

# Part A: the tiny test, [H, S, V] pixels with hues 0, 5, 120, 175, 178
tiny = np.array([[[0,   255, 255],
                  [5,   255, 255],
                  [120, 255, 255],
                  [175, 255, 255],
                  [178, 255, 255]]], dtype=np.uint8)

low = cv2.inRange(tiny, np.array([0, 100, 100]), np.array([10, 255, 255]))
high = cv2.inRange(tiny, np.array([170, 100, 100]), np.array([179, 255, 255]))
both = cv2.bitwise_or(low, high)

print("low red range  :", low[0])
print("high red range :", high[0])
print("combined       :", both[0])

# Part B: the real colour bars
img = cv2.imread("images/02_colour_bars.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low = cv2.inRange(hsv, np.array([0, 100, 100]), np.array([10, 255, 255]))
high = cv2.inRange(hsv, np.array([170, 100, 100]), np.array([179, 255, 255]))
mask_red = cv2.bitwise_or(low, high)
result = cv2.bitwise_and(img, img, mask=mask_red)

print()
print("mask at red bar     :", mask_red[100, 550])
print("mask at magenta bar :", mask_red[100, 450])
print("white pixels        :", np.count_nonzero(mask_red))

cv2.imshow("original", img)
cv2.imshow("red mask", mask_red)
cv2.imshow("red only", result)
cv2.waitKey(0)
cv2.destroyAllWindows()