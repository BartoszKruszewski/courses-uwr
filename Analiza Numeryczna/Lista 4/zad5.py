from test_range import test_range, get_e

def newton(a, x0):
    e = get_e()
    xn = x0
    i = 0
    while abs(xn - 1 / a) >= e and abs(xn - xn * (2 - xn * a)) >= e:
        i += 1
        xn = xn * (2 - xn * a)
        if abs(xn) > 10 ** 6:
            return 0
    return i

A = 2
for x0 in test_range(100):
    i = newton(A, x0)
    print(x0, 'inf' if i == 0 else i)

# dla 0 < x < (1 / A) dziala elegancko,
# oprocz tego sa jakies losowe przypadki gdzie dziala