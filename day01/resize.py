import cv2
import numpy as np


img = cv2.imread("images/02_colour_bars.png")

print("Shape:", img.shape)

resized = cv2.resize(img,(200,400))
print("Shape:", resized.shape)


cv2.imshow("Image",img)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()