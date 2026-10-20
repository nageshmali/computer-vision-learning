import cv2

specks = cv2.imread("images/noisy_specks.png")
fixed = cv2.medianBlur(specks, 5)

y, x = 57, 140                               # a pixel that has a white speck

window = specks[y - 2:y + 3, x - 2:x + 3, 0] # the 5 x 5 square, BLUE values only (channel 0)
print("the 5 x 5 square (blue values):")
print(window)

values = sorted(window.flatten().tolist())   # 25 numbers, smallest to largest
print("sorted:", values)
print("the middle one (13th of 25):", values[12])
print("medianBlur says            :", fixed[y, x, 0])