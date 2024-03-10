r = 18
f1 = 1
f2 = 1
while f2 < r:
    p = f2
    f2 += f1
    f1 = p
while f2 > 0 and r > 0:
    if f2 <= r:
        print(f2)
        r -= f2
    p = f1
    f1 = f2 - f1
    f2 = p