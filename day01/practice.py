import numpy as np
import cv2

img = cv2.imread("images/02_colour_bars.png")

print("Shape is ", img.shape)

img[250:450, 300:400] = [123, 123, 123]

cv2.imshow("demo",img)
cv2.waitKey(0)
cv2.destroyAllWindows()