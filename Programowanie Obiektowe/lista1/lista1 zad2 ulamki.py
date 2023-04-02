# Bartosz Kruszewski
# zad 2 lista 1 z PO: ułamki
# Python 3.11

# W Pythonie nie ma "struct", więc w tym programie zasymulowałem go za pomocą "class" bez użycia metod.
# Python nie jest dobrze przystosowany do takiego rozwiązanie co skutkuje koniecznością użcyia __new__() podczas
# deklarowania nowej "struktury".

class Fraction:
    nominator = 0
    denominator = 0


def new_fraction(nominator, denominator):
    f = Fraction.__new__(Fraction)  # wcześniej wspomniane deklarowanie nowej struktury
    f.nominator = nominator
    f.denominator = denominator
    shorten(f)
    return f


def shorten(f):
    def get_gcd(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    gcd = get_gcd(f.nominator, f.denominator)
    f.nominator //= gcd
    f.denominator //= gcd


def show(f):
    print(f.nominator, "/", f.denominator)


def add_fractions1(f1, f2):
    return new_fraction(f1.nominator * f2.denominator + f2.nominator * f1.denominator, f1.denominator * f2.denominator)


def sub_fractions1(f1, f2):
    return new_fraction(f1.nominator * f2.denominator - f2.nominator * f1.denominator, f1.denominator * f2.denominator)


def mult_fractions1(f1, f2):
    return new_fraction(f1.nominator * f2.nominator, f1.denominator * f2.denominator)


def div_fractions1(f1, f2):
    return new_fraction(f1.nominator * f2.denominator, f1.denominator * f2.nominator)


def add_fractions2(f1, f2):
    nominator = f1.nominator * f2.denominator + f2.nominator * f1.denominator
    denominator = f1.denominator * f2.denominator
    f2.nominator = nominator
    f2.denominator = denominator


def sub_fractions2(f1, f2):
    nominator = f1.nominator * f2.denominator - f2.nominator * f1.denominator
    denominator = f1.denominator * f2.denominator
    f2.nominator = nominator
    f2.denominator = denominator


def mult_fractions2(f1, f2):
    nominator = f1.nominator * f2.nominator
    denominator = f1.denominator * f2.denominator
    f2.nominator = nominator
    f2.denominator = denominator


def div_fractions2(f1, f2):
    nominator = f1.nominator * f2.denominator
    denominator = f1.denominator * f2.nominator
    f2.nominator = nominator
    f2.denominator = denominator


F1 = new_fraction(1, 2)
F2 = new_fraction(1, 3)
add_fractions2(F1, F2)
show(F2)
