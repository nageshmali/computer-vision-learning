import cv2
img = cv2.imread("images/02_colour_bars.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("colour shape:", img.shape)
print("gray shape  :", gray.shape)

print("green stripe:", gray[100, 350])
print("red stripe  :", gray[100, 550])
print("blue stripe :", gray[100, 650])

cv2.imshow("colour", img)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()