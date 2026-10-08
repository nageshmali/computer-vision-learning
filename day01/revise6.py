import cv2
import numpy as np

small = np.zeros((200, 300, 3), dtype=np.uint8)   # 200 rows, 300 columns, black
small[50:100, 100:200] = [0, 0, 255]              # red block
small[120:200, 180:300] = [255, 0, 0]             # blue block

print(small[75, 125])
print(small[150, 250])
print(small[0, 0])
print(small[120:200, 180:300].shape)

cv2.imshow("small", small)
cv2.waitKey(0)
cv2.destroyAllWindows()