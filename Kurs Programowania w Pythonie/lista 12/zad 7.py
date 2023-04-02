class Fraction:
    def __init__(self, n, dn):
        self.nominator = n
        self.denominator = dn
        self.shorten()

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
        return Fraction(self.nominator * other.nominator,  other.denominator * self.denominator)

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator,  other.nominator * self.denominator)

    def __str__(self):
        return str(self.nominator) + "/" + str(self.denominator)

    def __gt__(self, other):
        return self.nominator * other.denominator > self.denominator * other.nominator

    def __eq__(self, other):
        return self.nominator * other.denominator == self.denominator * other.nominator
