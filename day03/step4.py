import cv2
import numpy as np

img = cv2.imread("images/06_landscape.jpg")

H, W = img.shape[:2]


# 1. centered crop
ch, cw = 200, 200
y1 = (H - ch) // 2
x1 = (W - ch) // 2

center = img[y1:y1+ch, x1:x1+cw]
print("y1, x1:", y1, x1, " center shape:", center.shape)


# 2. crop from (x, y, w, h)
x, y, w, h = 100, 300, 250, 150
box = img[y:y + h, x:x + w]
print("box shape:", box.shape)

# 3. a crop is a view
view = img[0:100, 0:100]
view[:] = 0
print("img[50, 50] after editing the view:", img[50, 50])

# 4. a crop with .copy() is safe
img2 = cv2.imread("images/06_landscape.jpg")
safe = img2[0:100, 0:100].copy()
safe[:] = 0
print("img2[50, 50] after editing the copy:", img2[50, 50])

cv2.imshow("center crop", center)
cv2.imshow("box crop", box)
cv2.imshow("img with its corner blacked out", img)
cv2.waitKey(0)
cv2.destroyAllWindows()