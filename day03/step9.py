import cv2

class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def crop(self, img):
        return img[self.y:self.y + self.h, self.x:self.x + self.w]

    # def __repr__(self):
    #     return f"Box(x={self.x}, y={self.y}, w={self.w}, h={self.h})"


img = cv2.imread("images/06_landscape.jpg")

a = Box(40, 60, 120, 80)
b = Box(0, 0, 50, 50)

print(a)
print("area of a:", a.area())
print("crop shape:", a.crop(img).shape)
print(b, "area:", b.area())

a.w = 200
print(a, "area:", a.area(), "crop shape:", a.crop(img).shape)
print("b.x =", b.x, " a.x =", a.x)