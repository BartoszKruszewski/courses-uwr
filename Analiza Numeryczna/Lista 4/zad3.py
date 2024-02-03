def bisection(a, b, f, n):
    m = (a + b) / 2
    if f(m) == 0 or n == 0:
        return m
    if f(a) * f(m) < 0:
        return bisection(a, m, f, n - 1)
    return bisection(m, b, f, n - 1)

F = lambda x: x - 0.49
A = 0
B = 1
ACC_VAL = 0.49

for i in range(1, 6):
    e = abs(2 ** (-i - 1) * (B - A))
    val = bisection(A, B, F, i)
    e_r = abs(ACC_VAL - val)
    print(i, e, e_r, val)

