import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: could not open the camera")
    raise SystemExit

print("width :", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("height:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("fps   :", cap.get(cv2.CAP_PROP_FPS))

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("no frame received, stopping")
        break

    count += 1
    if count == 1:
        print("frame shape:", frame.shape, " dtype:", frame.dtype)

    frame = cv2.flip(frame, 1)
    cv2.putText(frame, "press q to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("camera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print("frames shown:", count)
cap.release()
cv2.destroyAllWindows()