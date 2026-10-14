import cv2
import numpy as np

canvas = np.zeros((220, 320, 3), dtype=np.uint8)
tri = np.array([[100, 40], [40, 180], [160, 180]], dtype=np.int32)
sq = np.array([[200, 60], [300, 60], [300, 160], [200, 160]], dtype=np.int32)

cv2.fillPoly(canvas, [tri, sq], (0, 255, 255))      # two polygons, one call

print(canvas[133, 100])     # inside the triangle
print(canvas[110, 250])     # inside the square
print(canvas[110, 180])     # between them