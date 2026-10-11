import cv2
import numpy as np

a = np.array([[0,100]], dtype=np.uint8)

print("NEAREST:", cv2.resize(a, (4,1), interpolation=cv2.INTER_NEAREST))
print("LINEAR :", cv2.resize(a, (4,1), interpolation=cv2.INTER_LINEAR))

b = np.array([[0, 100, 0, 100]], dtype=np.uint8)   # one row, four pixels
print("shrink NEAREST:", cv2.resize(b, (2, 1), interpolation=cv2.INTER_NEAREST))
print("shrink AREA   :", cv2.resize(b, (2, 1), interpolation=cv2.INTER_AREA))


icon = cv2.imread("images/04_icon_64.png")
print("IconShape:", icon.shape)
nearest = cv2.resize(icon, (512, 512), interpolation=cv2.INTER_NEAREST)
linear = cv2.resize(icon, (512, 512), interpolation=cv2.INTER_LINEAR)
cubic = cv2.resize(icon, (512, 512), interpolation=cv2.INTER_CUBIC)

for name, im in [("nearest", nearest), ("linear", linear), ("cubic", cubic)]:
    colours = len(np.unique(im.reshape(-1, 3), axis=0))
    print(name, "shape:", im.shape, " different colours:", colours)

cv2.imshow("nearest", nearest)
cv2.imshow("linear", linear)
cv2.imshow("cubic", cubic)
cv2.waitKey(0)
cv2.destroyAllWindows()