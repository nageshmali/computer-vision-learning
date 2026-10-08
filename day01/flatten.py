import cv2
import numpy as np


img = cv2.imread("images/02_colour_bars.png")
print("Shape is : ", img.shape)
print("Size is : ", img.size)
print("ndim is : ", img.ndim)

# Flatten to 1D
flatImg = img.flatten()
print("Shape is : ", flatImg.shape)
print("ndim is : ", flatImg.ndim)
print("first 9 numbers:", flatImg[:9])

# Restore using the remembered shape
restored = flatImg.reshape(img.shape)
print("restored shape:", restored.shape)
print("restored identical to original:", np.array_equal(img, restored))

# What if we use the WRONG shape?
wrong = flatImg.reshape(800, 600, 3)
print("wrong shape:", wrong.shape)
print("wrong identical to original:", np.array_equal(img, wrong))


cv2.imshow("original", img)
cv2.imshow("flattend", flatImg)
cv2.imshow("restored", restored)
cv2.imshow("wrong shape", wrong)
cv2.waitKey(0)
cv2.destroyAllWindows()