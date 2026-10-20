import cv2

specks = cv2.imread("images/noisy_specks.png")

fixed = cv2.medianBlur(specks,5)

cv2.imshow("before: specks", specks)
cv2.imshow("after: median", fixed)
cv2.waitKey(0)
cv2.destroyAllWindows()