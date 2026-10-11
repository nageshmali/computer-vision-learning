import cv2
import numpy as np

# Part A: a black 300 x 300 image with a white block at the TOP-RIGHT
img = np.zeros((300, 300, 3), dtype=np.uint8)
img[10:30, 270:290] = 255
H, W = img.shape[:2]
center = (W / 2, H / 2)

M = cv2.getRotationMatrix2D(center, 90, 1.0)
print("matrix for 90 degrees:")
print(np.round(M, 2))

rot = cv2.warpAffine(img, M, (W, H))
ys, xs = np.nonzero(rot[:, :, 0])
print("after +90: white block rows", ys.min(), "to", ys.max(),
      " columns", xs.min(), "to", xs.max())

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rot = cv2.warpAffine(img, M, (W, H))
ys, xs = np.nonzero(rot[:, :, 0])
print("after -90: white block rows", ys.min(), "to", ys.max(),
      " columns", xs.min(), "to", xs.max())

# Part B: rotate the landscape by 45 degrees
land = cv2.imread("images/06_landscape.jpg")
H, W = land.shape[:2]
M45 = cv2.getRotationMatrix2D((W / 2, H / 2), 45, 1.0)
rot45 = cv2.warpAffine(land, M45, (W, H))

print("rotated shape:", rot45.shape)
print("centre pixel before:", land[H // 2, W // 2], " after:", rot45[H // 2, W // 2])
print("top-left corner after:", rot45[0, 0])

cv2.imshow("original", land)
cv2.imshow("rotated 45", rot45)
cv2.waitKey(0)
cv2.destroyAllWindows()