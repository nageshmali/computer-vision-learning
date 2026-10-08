import numpy as np

img = np.array([
    [56,41,134,23],
    [1,34,212,31],
    [143,234,1,12],
], dtype=np.uint8)


print(img)
print("Shape = ",img.shape)
print("dtype = ", img.dtype)
print("Size = ", img.size)
print("ndim = ", img.ndim)
print("pixel at row 1, column 2:", img[1, 2])
print("first row:", img[0])

