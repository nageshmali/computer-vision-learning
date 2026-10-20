import cv2

grain = cv2.imread("images/noisy_grain.png")

box = cv2.blur(grain, (5, 5))
gauss = cv2.GaussianBlur(grain, (5, 5), 0)
median = cv2.medianBlur(grain, 5)
bilat = cv2.bilateralFilter(grain, 9, 75, 75)

clean = cv2.imread("images/06_landscape.jpg")

for name, im in [("clean", clean), ("grain", grain), ("box", box),
                 ("gaussian", gauss), ("median", median), ("bilateral", bilat)]:
    patch = im[10:60, 10:200, 0]
    print(f"{name:10s} how much the sky wiggles: {patch.std():.1f}")

cv2.imshow("0 original grain", grain)
cv2.imshow("1 box", box)
cv2.imshow("2 gaussian", gauss)
cv2.imshow("3 median", median)
cv2.imshow("4 bilateral", bilat)
cv2.waitKey(0)
cv2.destroyAllWindows()