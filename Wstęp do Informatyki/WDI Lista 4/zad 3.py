def NWD(a, b):
    while (b != 0):
        pom = b
        b = a % b
        a = pom
    return a


def NWD_ciagu(n, tab):
    nwd = NWD(tab[0], tab[1])
    for i in range(2, n):
        nwd = NWD(nwd, tab[i])
    return nwd


n = int(input())
tab = [0] * n
for i in range(n):
    tab[i] = int(input())
print(NWD_ciagu(n, tab))
