import cv2
import numpy as np

a = np.full((2, 2, 3), 250, dtype=np.uint8)   # tiny image, every number is 250
b = np.full((2, 2, 3), 10, dtype=np.uint8)    # tiny image, every number is 10

print("numpy a + b :", (a + b)[0, 0])
print("cv2.add     :", cv2.add(a, b)[0, 0])

img = cv2.imread("images/07_gray_gradient.jpg")
more = np.full_like(img, 100)          # same shape as img, every number 100

wrapped = img + more
saturated = cv2.add(img, more)

cv2.imshow("original", img)
cv2.imshow("more", more)
cv2.imshow("img + more (wraps)", wrapped)
cv2.imshow("cv2.add (saturates)", saturated)
cv2.waitKey(0)
cv2.destroyAllWindows()