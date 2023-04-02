def czy_ukladane(a, b):
    litery_a = ile_liter(a)
    litery_b = ile_liter(b)
    for i in litery_a:
        if not (i in litery_b and litery_a[i] <= litery_b[i]):
            return False
    return True


def ile_liter(a):
    litery = {}
    for i in a:
        if i not in litery:
            litery[i] = 1
        else:
            litery[i] += 1
    return litery

print(czy_ukladane("kot","lokomotywa"))
