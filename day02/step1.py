import cv2
import numpy as np

img = cv2.imread("images/02_colour_bars.png")

print("white bar:", img[100, 50])
print("red bar  :", img[100, 550])
print("blue bar :", img[100, 650])