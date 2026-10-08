import cv2
from pathlib import Path

folder = Path("images")
allowed = [".jpg",".jpeg",".png"]

paths = sorted(p for p in folder.iterdir() if p.suffix.lower() in allowed)
print("Found", len(paths), "image files")
print()

loaded = []

for number,path in enumerate(paths,start=1):
    img = cv2.imread(str(path))
    if img is None:
        print(f"{number}. SKIPPED (could not load): {path.name}")
        continue
    loaded.append(img)
    print(f"{number}. {path.name}")
    print("   shape:", img.shape)
    print("   dtype:", img.dtype)
    print("   size :", img.size)
    print("   ndim :", img.ndim)

print()
print("Loaded", len(loaded), "images successfully")