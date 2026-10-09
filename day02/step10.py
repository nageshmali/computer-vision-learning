# A. scope
x = 10
def change():
    x = 5
    return x
print("A:", change(), x)

# B. the default-argument trap
def add_item(item, box=[]):
    box.append(item)
    return box
print("B1:", add_item("a"))
print("B2:", add_item("b"))

def add_item_fixed(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box
print("B3:", add_item_fixed("a"))
print("B4:", add_item_fixed("b"))

# C. *args and **kwargs
def total(*args):
    return sum(args)
print("C1:", total(1, 2, 3))
print("C2:", total(10, 20, 30, 40))

def info(*args, **kwargs):
    print("C3 args  :", args)
    print("C3 kwargs:", kwargs)
info(1, 2, color="red", value=255)

# D. lambda
square = lambda n: n * n
print("D1:", square(5))
pairs = [("red", 76), ("green", 150), ("blue", 29)]
print("D2:", sorted(pairs, key=lambda p: p[1]))

# E. comprehensions
nums = [1, 2, 3, 4, 5, 6]
print("E1:", [n * n for n in nums])
print("E2:", [n for n in nums if n % 2 == 0])
print("E3:", {n: n * n for n in nums})