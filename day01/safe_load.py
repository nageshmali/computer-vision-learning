import cv2

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        print(f"ERROR: could not load image from '{path}'")
        print("Check the file name, the extension and the folder.")
        return None
    return img

# Test 2: a file name that does not exist
img = load_image("images/does_not_exist.jpg")
print("Test 1 result:", img)

# Test 2:real photo
img = load_image("images/photo1.png")
print("Test 2 Done:, shape is = ", img.shape)