import cv2
import os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: could not open the camera")
    raise SystemExit

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30

ret, frame = cap.read()
h, w = frame.shape[:2]
print("frame size (w, h):", (w, h), " fps:", fps)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("clip.mp4", fourcc, fps, (w, h))
print("writer opened:", out.isOpened())

total = int(5 * fps)               # 5 seconds of frames
count = 0
while count < total:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
    cv2.putText(frame, f"REC {count}", (50, 38), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 0, 255), 2, cv2.LINE_AA)
    out.write(frame)
    cv2.imshow("recording", frame)
    count += 1
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
cap.release()
cv2.destroyAllWindows()

print("frames written:", count)
print("file size:", os.path.getsize("clip.mp4"), "bytes")

check = cv2.VideoCapture("clip.mp4")
print("clip width :", check.get(cv2.CAP_PROP_FRAME_WIDTH))
print("clip height:", check.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("clip fps   :", check.get(cv2.CAP_PROP_FPS))
print("clip frames:", check.get(cv2.CAP_PROP_FRAME_COUNT))
check.release()

# the size-mismatch trap on purpose
bad = cv2.VideoWriter("bad.mp4", fourcc, fps, (w, h))
small = cv2.resize(frame, (w // 2, h // 2))
for _ in range(30):
    bad.write(cv2.resize(small, (w, h)))
bad.release()
print("bad file size:", os.path.getsize("bad.mp4"), "bytes")