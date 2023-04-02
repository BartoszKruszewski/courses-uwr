def fTrec(n, m):
    if m == 0:
        return n
    elif n == 0:
        return m
    else:
        return fTrec(n - 1, m) + 2 * fTrec(n, m - 1)

print(fTrec(3, 4))