import cv2
import numpy as np

tiny = np.array([
    [1,2,3],
    [4,5,6],
],dtype=np.uint8)

print("flip 1 :", cv2.flip(tiny, 1).tolist())
print("flip 0 :", cv2.flip(tiny, 0).tolist())
print("flip -1:", cv2.flip(tiny, -1).tolist())

print("slice [:, ::-1]   equals flip 1 :", np.array_equal(cv2.flip(tiny, 1), tiny[:, ::-1]))
print("slice [::-1]      equals flip 0 :", np.array_equal(cv2.flip(tiny, 0), tiny[::-1]))
print("slice [::-1, ::-1] equals flip -1:", np.array_equal(cv2.flip(tiny, -1), tiny[::-1, ::-1]))


img = cv2.imread("images/06_landscape.jpg")
left_right = cv2.flip(img, 1)
up_down = cv2.flip(img, 0)
both = cv2.flip(img, -1)

print("shape unchanged:", img.shape, left_right.shape)
cv2.imshow("original", img)
cv2.imshow("left-right", left_right)
cv2.imshow("up-down", up_down)
cv2.imshow("both", both)
cv2.waitKey(0)
cv2.destroyAllWindows()