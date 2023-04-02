def max_p(n, a):
    p = 1
    x = a
    i = 1
    while x < n:
        if n % x == 0:
            p = i
        i += 1
        x *= a
    return p


def czysc_tab(tab, k):
    for i in range(k):
        tab[i] = 0


n = int(input())
k = int(input())
tab = [0] * k
m = 0
l = 0
for i in range(k):
    a = int(input())
    p = max_p(n, a)
    if p > m:
        m = p
        czysc_tab(tab, k)
        tab[0] = a
        l = 1
    elif p == m:
        tab[l] = a
        l += 1

print(p)
for i in range(k):
    if tab[i] > 0:
        print(tab[i])
