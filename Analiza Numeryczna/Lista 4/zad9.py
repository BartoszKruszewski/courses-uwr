from test_range import test_range

def derivative(f):
    H = 10 ** - 6
    return lambda x: (f(x + H) - f(x)) / H

def newton(x0, r, f, n = 100):
    xn = x0
    for _ in range(n):
        xn -= r * f(xn) / derivative(f)(xn)
    return xn

X0 = 10
R = 5   

for a in test_range(100):
    f = lambda x: (x - a) ** R
    result = newton(X0, R, f)
    print(f'{a}: {abs((result - a) / a * 100):.0f}%')