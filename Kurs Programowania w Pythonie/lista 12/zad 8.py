class Fraction:
    def __init__(self, n, dn):
        self.nominator = n
        self.denominator = dn

    def get_decimal(self):
        return self.nominator // self.denominator

    def shorten(self):
        def get_nwd(a, b):
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return a

        nwd = get_nwd(self.nominator, self.denominator)
        self.nominator //= nwd
        self.denominator //= nwd

    def __add__(self, other):
        return Fraction(self.nominator * other.denominator + other.nominator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.nominator * other.denominator - other.nominator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator, other.denominator * self.denominator)

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator, other.nominator * self.denominator)

    def __str__(self):
        return str(self.nominator) + "/" + str(self.denominator)

    def __gt__(self, other):
        return self.nominator * other.denominator > self.denominator * other.nominator

    def __eq__(self, other):
        return self.nominator * other.denominator == self.denominator * other.nominator


def strong(a):
    result = 1
    x = 1
    for i in range(1, a):
        x += 1
        result *= x
    return result


def get_s(n):
    S = [True] * n
    S[0] = False
    S[1] = False
    for i in range(2, n):
        if S[i]:
            for j in range(i * i, n, i):
                S[j] = False
    return S

s = get_s(1000000)
precision = 100
e = Fraction(1, 1)
for i in range(1, precision):
    e += Fraction(1, strong(i))
    e.shorten()
digits = str(e.nominator * 10**1000 // e.denominator)

i = 0
while not s[int(digits[i:i+5])]:
    i += 1
print(digits[i:i+5])