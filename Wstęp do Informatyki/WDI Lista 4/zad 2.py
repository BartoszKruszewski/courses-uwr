def NWD(a, b):
    while (b != 0):
        pom = b
        b = a % b
        a = pom
    return a


def NWW(a, b):
    return a * b // NWD(a, b)


def uproszczenie(a, b):
    nwd = NWD(a, b)
    return a // nwd, b // nwd


print(uproszczenie(10, 24))
