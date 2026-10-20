import cv2

specks = cv2.imread("images/noisy_specks.png")

box = cv2.blur(specks, (5, 5))
gauss = cv2.GaussianBlur(specks, (5, 5), 0)
median = cv2.medianBlur(specks, 5)
bilat = cv2.bilateralFilter(specks, 9, 75, 75)

cv2.imshow("0 original specks", specks)
cv2.imshow("1 box", box)
cv2.imshow("2 gaussian", gauss)
cv2.imshow("3 median", median)
cv2.imshow("4 bilateral", bilat)
cv2.waitKey(0)
cv2.destroyAllWindows()