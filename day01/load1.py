import cv2

img = cv2.imread("images/photo1.png")

print("type:", type(img))
print("shape:", img.shape)
print("size:", img.size)
print("dtype:", img.dtype)
print("ndim:", img.ndim)


cv2.imshow("My first image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()