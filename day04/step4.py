import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
text = "Hgllo CV"

for scale in (0.5, 1, 2):
    (w, h), base = cv2.getTextSize(text, font, scale, 1)
    print("scale", scale, "-> width", w, " height", h, " baseline", base)

canvas = np.zeros((300, 600, 3), dtype=np.uint8)

(w, h), base = cv2.getTextSize(text, font, 2, 3)
x, y = 50, 100
cv2.putText(canvas, text, (x, y), font, 2, (255, 255, 255), 3, cv2.LINE_AA)
cv2.rectangle(canvas, (x, y - h), (x + w, y + base), (0, 255, 0), 1)
print("size:", (w, h), "baseline:", base)

# the same text, centred in the canvas
H, W = canvas.shape[:2]
cx = (W - w) // 2
cy = (H + h) // 2
cv2.putText(canvas, text, (cx, cy), font, 2, (0, 255, 255), 3, cv2.LINE_AA)
print("centred origin:", (cx, cy))

# text whose baseline is too close to the top
cv2.putText(canvas, "TOP", (400, 20), font, 2, (0, 0, 255), 3)

cv2.imshow("text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()