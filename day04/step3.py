import cv2
import numpy as np

canvas = np.zeros((450, 700, 3), dtype=np.uint8)

# a filled triangle
tri = np.array([[100, 40], [40, 180], [160, 180]], dtype=np.int32)
cv2.fillPoly(canvas, [tri], (0, 255, 255))

# a pentagon outline: closed, and an open copy shifted 220 pixels to the right
P = np.array([[60, 260], [120, 230], [180, 260], [160, 350], [80, 350]], dtype=np.int32)
cv2.polylines(canvas, [P], True, (255, 0, 0), 2)
cv2.polylines(canvas, [P + [220, 0]], False, (255, 0, 0), 2)


# two filled ellipses: one flat, one rotated by 90 degrees
cv2.ellipse(canvas, (500, 100), (100, 50), 0, 0, 360, (0, 255, 0), -1)
cv2.ellipse(canvas, (500, 280), (100, 50), 90, 0, 360, (0, 0, 255), -1)

# the bottom half of an ellipse outline
cv2.ellipse(canvas, (350, 400), (80, 30), 0, 0, 180, (255, 255, 255), 3)

checks = {
    "inside triangle  [133, 100]": (133, 100),
    "outside triangle [133, 200]": (133, 200),
    "closed pentagon edge [305, 70]": (305, 70),
    "open pentagon, same edge [305, 290]": (305, 290),
    "flat ellipse centre [100, 500]": (100, 500),
    "flat ellipse, 90 right [100, 590]": (100, 590),
    "flat ellipse, 110 right [100, 610]": (100, 610),
    "flat ellipse, 45 below [145, 500]": (145, 500),
    "flat ellipse, 55 below [155, 500]": (155, 500),
    "rotated ellipse, 70 below [350, 500]": (350, 500),
    "rotated ellipse, 70 right [280, 570]": (280, 570),
    "arc bottom [430, 350]": (430, 350),
    "arc top [370, 350]": (370, 350),
}

for name, (y, x) in checks.items():
    print(name, canvas[y, x])

cv2.imshow("polygons and ellipses", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

