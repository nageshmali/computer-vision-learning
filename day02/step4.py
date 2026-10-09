import cv2

img = cv2.imread("images/02_colour_bars.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print("red bar  :", hsv[100, 550])
print("blue bar :", hsv[100, 650])
print("white bar:", hsv[100, 50])