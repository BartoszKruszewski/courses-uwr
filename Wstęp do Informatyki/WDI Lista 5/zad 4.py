def G(n):
    a = 1
    b = 1
    c = 1
    x = a + b + c
    for i in range(n-3):
        c = b
        b = a
        a = x
        x = a + b +c
    return x