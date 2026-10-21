import cv2
import numpy as np

kernel = np.array([[ 0, -1,  0],
                   [-1,  5, -1],
                   [ 0, -1,  0]], dtype=np.float32)
print("kernel adds up to:", kernel.sum())

# the same speck grid
img = np.full((5, 5), 10, dtype=np.uint8)
img[2, 2] = 90
print("speck grid after sharpening:")
print(cv2.filter2D(img, -1, kernel))

# the same edge grid
edge = np.array([[10, 10, 10, 90, 90, 90]] * 5, dtype=np.uint8)
print("edge row after sharpening:")
print(cv2.filter2D(edge, -1, kernel)[2])