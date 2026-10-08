data = list(range(100))   # 100 pretend images

train = data[:70]
val = data[70:85]
test = data[85:]

print("train:", len(train), "first:", train[0], "last:", train[-1])
print("val  :", len(val), "first:", val[0], "last:", val[-1])
print("test :", len(test), "first:", test[0], "last:", test[-1])