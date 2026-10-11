import cv2

img = cv2.imread("images/06_landscape.jpg")
print("original shape:", img.shape)

half = cv2.resize(img, (512,384))
print("half shape:", half.shape)

by_scale = cv2.resize(img, None, fx=0.5, fy=0.5)
print("by scale shape   :", by_scale.shape)

wrong = cv2.resize(img, (384, 512))
print("wrong-order shape:", wrong.shape)

cv2.imshow("original", img)
cv2.imshow("half", half)
cv2.imshow("by_scale", by_scale)
cv2.imshow("wrong order", wrong)
cv2.waitKey(0)
cv2.destroyAllWindows()