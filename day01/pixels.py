import cv2

img = cv2.imread("images/02_colour_bars.png")
print("Shape is =", img.shape)

# Read single pixels: img[row, column]
print("row 100, col 50 :", img[100, 50])
print("row 100, col 250:", img[100, 250])
print("row 100, col 350:", img[100, 350])
print("row 100, col 550:", img[100, 550])
print("row 100, col 650:", img[100, 650])
print("row 100, col 750:", img[100, 750])

# Read the three channels of one pixel separately
b, g, r = img[100, 550]
print("blue =", b, " green =", g, " red =", r)

# Change a region on a COPY
edited = img.copy()
edited[50:150, 450:550] = [0, 165, 255] # orange square (B, G, R)


print("original still unchanged:", img[100, 450])
print("edited pixel changed    :", edited[100, 450])

print(img[100, 550])

