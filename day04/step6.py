import cv2
import time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: could not open the camera")
    raise SystemExit

prev = time.perf_counter()
fps = 0.0
heavy = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)

    if heavy:
        frame = cv2.bilateralFilter(frame, 15, 80, 80)    # a slow filter

    now = time.perf_counter()
    inst = 1.0 / (now - prev)
    prev = now
    fps = 0.9 * fps + 0.1 * inst

    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2, cv2.LINE_AA)
    label = "heavy filter: " + ("ON" if heavy else "OFF") + "  (press h)"
    cv2.putText(frame, label, (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("fps", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("h"):
        heavy = not heavy

cap.release()
cv2.destroyAllWindows()