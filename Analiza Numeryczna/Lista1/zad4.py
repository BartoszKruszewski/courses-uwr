def y(n):
    return y_rec(n, [1, -1 /9])

def y_rec(n, l):
    if (len(l) > n):
        return l[n]
    result = (80 / 9) * y_rec(n - 1, l) + y_rec(n - 2, l)
    l.append(result)
    return result

for i in range(2, 51):
    print(y(i))