import cv2

img = cv2.imread("images/02_colour_bars.png")

b,g,r = cv2.split(img)

print("colour image shape:", img.shape)
print("blue sheet shape  :", b.shape)

cv2.imshow("original", img)
cv2.imshow("blue sheet", b)
cv2.imshow("green sheet", g)
cv2.imshow("red sheet", r)
cv2.waitKey(0)
cv2.destroyAllWindows()