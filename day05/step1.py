import cv2

clean = cv2.imread("images/06_landscape.jpg")
specks = cv2.imread("images/noisy_specks.png")
grain = cv2.imread("images/noisy_grain.png")

cv2.imshow("clean", clean)
cv2.imshow("specks", specks)
cv2.imshow("grain", grain)
cv2.waitKey(0)
cv2.destroyAllWindows()