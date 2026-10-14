import cv2

img = cv2.imread("images/02_colour_bars.png")
canvas = img.copy()

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        print(f"clicked at x={x}, y={y}   pixel (B, G, R) = ({b}, {g}, {r})")
        cv2.circle(canvas, (x, y), 8, (255, 255, 255), 2)

cv2.namedWindow("click me")
cv2.setMouseCallback("click me", on_mouse)

while True:
    cv2.imshow("click me", canvas)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()