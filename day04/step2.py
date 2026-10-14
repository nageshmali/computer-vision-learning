import cv2
import numpy as np

canvas = np.zeros((400,600,3), dtype=np.uint8)


cv2.line(canvas, (50, 50), (550, 50), (0, 255, 0), 3) 
cv2.rectangle(canvas, (100, 100), (300, 250), (255, 0, 0), 2) 
cv2.rectangle(canvas, (350, 100), (500, 250), (0, 0, 255), -1) 
cv2.circle(canvas, (200, 320), 50, (0, 255, 255), -1) 
cv2.circle(canvas, (450, 320), 60, (255, 255, 255), 4) 
print("on the line    [50, 300]  :", canvas[50, 300])
print("blue edge      [100, 200] :", canvas[100, 200])
print("inside outline [175, 200] :", canvas[175, 200])
print("inside red     [175, 400] :", canvas[175, 400])
print("yellow centre  [320, 200] :", canvas[320, 200])
print("ring centre    [320, 450] :", canvas[320, 450])
print("on the ring    [320, 510] :", canvas[320, 510])

red = np.all(canvas == [0, 0, 255], axis=2)
print("red pixels:", int(red.sum()))

saved = cv2.imwrite("images/shapes.png", canvas)
print("saved:", saved)

cv2.imshow("shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()