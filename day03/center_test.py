import cv2

land = cv2.imread("images/06_landscape.jpg")
H, W = land.shape[:2]

good = cv2.warpAffine(land, cv2.getRotationMatrix2D((W / 2, H / 2), 30, 1.0), (W, H))
bad = cv2.warpAffine(land, cv2.getRotationMatrix2D((H / 2, W / 2), 30, 1.0), (W, H))

print("original centre pixel     :", land[H // 2, W // 2])
print("after good centre (W/2,H/2):", good[H // 2, W // 2])
print("after swapped centre (H/2,W/2):", bad[H // 2, W // 2])