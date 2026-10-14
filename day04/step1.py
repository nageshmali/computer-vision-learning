import cv2
import numpy as np
import os

img = cv2.imread("images/06_landscape.jpg")

ok = cv2.imwrite("images/out.png", img)
print("png saved:", ok, " size:", os.path.getsize("images/out.png"), "bytes")

for q in (90, 50, 10):
    name = f"out_q{q}.jpg"
    cv2.imwrite(name, img, [cv2.IMWRITE_JPEG_QUALITY, q])
    print(name, "size:", os.path.getsize(name), "bytes")

png = cv2.imread("images/out.png")
print("png identical to original:", np.array_equal(png, img))

for q in (90, 50, 10):
    jpg = cv2.imread(f"out_q{q}.jpg")
    diff = np.abs(jpg.astype(int) - img.astype(int))
    print(f"jpg q{q}: identical? {np.array_equal(jpg, img)}   biggest difference: {diff.max()}")

bad = cv2.imwrite("no_such_folder/x.png", img)
print("save into a missing folder returned:", bad)