import cv2
import numpy as np

def rotate_full(img, angle):
    H, W = img.shape[:2]
    cx, cy = W / 2, H / 2

    M = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)

    cos = abs(M[0, 0])
    sin = abs(M[0, 1])

    new_w = int(H * sin + W * cos)
    new_h = int(H * cos + W * sin)

    M[0, 2] += new_w / 2 - cx
    M[1, 2] += new_h / 2 - cy

    return cv2.warpAffine(img, M, (new_w, new_h))

# Part A: shapes
land = cv2.imread("images/06_landscape.jpg")
print("original shape:", land.shape)
for a in (90, 45, 30):
    print("angle", a, "->", rotate_full(land, a).shape)

# Part B: is anything lost? Count the white pixels of a white 200 x 100 rectangle
white = np.full((100, 200, 3), 255, dtype=np.uint8)
print("original white pixels:", 100 * 200)

H, W = white.shape[:2]
M = cv2.getRotationMatrix2D((W / 2, H / 2), 45, 1.0)
naive = cv2.warpAffine(white, M, (W, H))
full = rotate_full(white, 45)

print("naive rotation  :", int((naive[:, :, 0] > 127).sum()))
print("full-canvas one :", int((full[:, :, 0] > 127).sum()))

cv2.imshow("naive 45", naive)
cv2.imshow("full 45", full)
cv2.imshow("landscape full 45", rotate_full(land, 45))
cv2.waitKey(0)
cv2.destroyAllWindows()