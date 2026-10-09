import cv2
import numpy as np

a = np.array([[255, 255, 0, 0]], dtype=np.uint8)
b = np.array([[255, 0, 255, 0]], dtype=np.uint8)

print("AND:", cv2.bitwise_and(a, b)[0])
print("OR :", cv2.bitwise_or(a, b)[0])