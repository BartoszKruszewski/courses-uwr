def generuj_sito(m,n):
    sito = [True] * n
    sito[0] = False
    sito[1] = False

    a = 2
    while a * a <= m:
        if sito[a]:
            for j in range(a*a,n,a):
                sito[j] = False
        a += 1

    for i in range(m,n):
        if sito[i]:
            for j in range(i*i,n,i):
                sito[j] = False
    return sito

sito = generuj_sito(1000,1100)
for i in range(1000,1100):
    if sito[i]:
        print(i)