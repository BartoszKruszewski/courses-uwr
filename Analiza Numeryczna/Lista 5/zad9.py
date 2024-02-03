from math import log
from decimal import Decimal, getcontext

def d(f):
    H = Decimal(10 ** - 6)
    return lambda x: (f(x + H) - f(x)) / H

def olver(f, x0, n = 10):
    
    values = []

    # obliczanie funkcji pochodnych
    df = d(f)
    ddf = d(df)

    # przypisanie x0
    xn = Decimal(x0)

    for _ in range(n):

        # zapamietanie wyniku dla kazdego kroku
        values.append(xn)

        # obliczanie wartosci funkcji
        fxn = f(xn)
        dfxn = df(xn)
        ddfxn = ddf(xn)

        # krok metody
        xn -= fxn / dfxn - Decimal(0.5) * ddfxn / dfxn * (fxn / dfxn) ** 2

    return values

def avg(l):
    return sum(l) / len(l)

def get_exponent(values, a):
    exponents = []
    for i in range(len(values) - 2):
        en1 = abs(values[i] - a)
        en2 = abs(values[i + 1] - a)
        en3 = abs(values[i + 2] - a)
        exponents.append((log(en3) - log(en2)) / (log(en2) - log(en1)))
    return sum(exponents) / len(exponents)

def test(f, correct_f):
    X0 = Decimal(1)
    return avg([get_exponent(
        olver(f(Decimal(a)), X0), Decimal(correct_f(Decimal(a))))
        for a in range(2, 100)
    ])

getcontext().prec = 256
for r in range(2, 10):  
    print(test(lambda a: lambda x: x ** Decimal(r) - a, lambda a: a ** (1 / Decimal(r))))