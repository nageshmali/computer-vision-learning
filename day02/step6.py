import cv2
import numpy as np

# a tiny image, 1 row and 5 pixels, each pixel is [H, S, V]
tiny = np.array([[[0,   255, 255],
                  [5,   255, 255],
                  [120, 255, 255],
                  [175, 255, 255],
                  [178, 255, 255]]], dtype=np.uint8)

lower = np.array([0, 100, 100])
upper = np.array([10, 255, 255])

mask = cv2.inRange(tiny, lower, upper)
print("hues     :", [0, 5, 120, 175, 178])
print("mask     :", mask[0])