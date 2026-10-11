import cv2
import numpy as np

img = cv2.imread("images/06_landscape.jpg")
H, W = img.shape[:2]

M = np.float32([
    [1,0,100],
    [0,1,50]
])
moved = cv2.warpAffine(img, M, (W, H))

print("img shape:", img.shape)
print("movedshape:", moved.shape)
print("original pixel [100, 200]:", img[100, 200])
print("same pixel after the move, at [150, 300]:", moved[150, 300])
print("top-left corner of moved :", moved[0, 0])
print("pixel [50, 100] of moved :", moved[50, 100], " original [0, 0]:", img[0, 0])

# slide left 100 and up 50
M2 = np.float32([[1, 0, -100],
                 [0, 1, -50]])
moved2 = cv2.warpAffine(img, M2, (W, H))
print("bottom-right corner of moved2:", moved2[H - 1, W - 1])

cv2.imshow("original", img)
cv2.imshow("right and down", moved)
cv2.imshow("left and up", moved2)
cv2.waitKey(0)
cv2.destroyAllWindows()