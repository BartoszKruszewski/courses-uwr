from math import log
from decimal import Decimal, getcontext

def get_exponent(values):
    exponents = []
    for i in range(len(values) - 2):
        en1 = values[i]
        en2 = values[i + 1]
        en3 = values[i + 2]
        exponents.append((log(en3) - log(en2)) / (log(en2) - log(en1)))
    return sum(exponents) / len(exponents)

def get_c(p, values):
    c = []
    for i in range(len(values) - 1):
        en1 = values[i]
        en2 = values[i + 1]
        c.append(en2 / en1 ** p)
    return sum(c) / len(c)

def get_iterations_number(p, c, values):
    getcontext().prec = 100
    en = Decimal(values[-1])
    i = len(values)
    while abs(en) >= Decimal(10 ** -100):
        i += 1
        en = (en * Decimal(c)) ** Decimal(p)
    return i

R_V = [
    0.763907023,
    0.543852762,
    0.196247370,
    0.009220859
]

A_V = [
    0.605426053,
    0.055322784,
    0.004819076,
    0.000399783
]

r_p = get_exponent(R_V)
a_p = get_exponent(A_V)

r_c = get_c(r_p, R_V)
a_c = get_c(a_p, A_V)

r_i = get_iterations_number(r_p, r_c, R_V)
a_i = get_iterations_number(a_p, a_c, A_V)

print(f'Rosjanie | p: {r_p} c: {r_c} i: {r_i}')
print(f'Amerykanie | p: {a_p} c: {a_c} i: {a_i}')

# Rosjanie ~ 3
# Amerykanie ~ 1

# Rosjanie maja wyzszy wykladnik zbieznosci,
# wiec oni beda pierwsi

