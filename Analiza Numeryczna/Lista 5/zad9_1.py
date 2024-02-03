from math import log
from decimal import Decimal, getcontext

getcontext().prec = 256

A_RANGE = 10
N = 5

def olver(f, df, ddf, x0 = 1, n = N):
    
    values = []
    xn = Decimal(x0)

    for _ in range(n):
        values.append(xn)

        fxn = f(xn)
        dfxn = df(xn)
        ddfxn = ddf(xn)

        xn -= fxn / dfxn - Decimal(0.5) * ddfxn / dfxn * (fxn / dfxn) ** 2

    return values

def get_exponent(values, a):
    exponents = []
    for i in range(len(values) - 2):
        en1 = abs(values[i] - a)
        en2 = abs(values[i + 1] - a)
        en3 = abs(values[i + 2] - a)
        exp = (log(en3) - log(en2)) / (log(en2) - log(en1))
        exponents.append(exp)
    return sum(exponents) / len(exponents)

def test(f, df, ddf, alfa):
    values = olver(f, df, ddf)
    return get_exponent(values, alfa)

# f(x) = x * x - A
def multiple_test_1():
    exponents = []
    for a in range(2, A_RANGE):
        exponents.append(test(
            lambda x: x * x - Decimal(a),
            lambda x: Decimal(2) * x,
            lambda x: Decimal(2),
            Decimal(a) ** Decimal(1 / 2)
        ))
    return sum(exponents) / len(exponents)

# f(x) = 1 / x - A
def multiple_test_2():
    exponents = []
    for a in range(2, A_RANGE):
        exponents.append(test(
            lambda x: 1 / x - Decimal(a),
            lambda x: Decimal(-1) / (x * x),
            lambda x: Decimal(2) / (x * x * x),
            Decimal(1 / a)
        ))
    return sum(exponents) / len(exponents)

# f(x) = 1 / (x * x) - A
def multiple_test_3():
    exponents = []
    for a in range(2, A_RANGE):
        exponents.append(test(
            lambda x: 1 / (x * x) - Decimal(a),
            lambda x: Decimal(-2) / (x * x * x),
            lambda x: Decimal(-6) / (x * x * x * x),
            Decimal(1) / (Decimal(a) ** Decimal(1 / 2))
        ))
    return sum(exponents) / len(exponents)

exponents = [
    multiple_test_1(),
    multiple_test_2(),
    multiple_test_3()
]

print(exponents)
print(sum(exponents) / len(exponents))
