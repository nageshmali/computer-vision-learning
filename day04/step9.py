import cv2
import numpy as np

canvas = np.zeros((480, 640, 3), dtype=np.uint8)
state = {"drawing": False, "last": None, "color": (0, 255, 0), "size": 4}


def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        state["drawing"] = True
        state["last"] = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and state["drawing"]:
        cv2.line(canvas, state["last"], (x, y), state["color"], state["size"])
        state["last"] = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        state["drawing"] = False


cv2.namedWindow("paint")
cv2.setMouseCallback("paint", on_mouse)

while True:
    view = canvas.copy()
    cv2.putText(view, "1 green  2 red  3 blue  c clear  s save  q quit", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("paint", view)

    key = cv2.waitKey(10) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("1"):
        state["color"] = (0, 255, 0)
    elif key == ord("2"):
        state["color"] = (0, 0, 255)
    elif key == ord("3"):
        state["color"] = (255, 0, 0)
    elif key == ord("c"):
        canvas[:] = 0
    elif key == ord("s"):
        ok = cv2.imwrite("painting.png", canvas)
        print("saved:", ok)

cv2.destroyAllWindows()