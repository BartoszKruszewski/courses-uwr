def wartosc(a,k):
    w = 0
    for i in range(k + 1):
        w = 2 * w + a[i - 1]
    return w

print(wartosc([1,1,0,1,0],5))