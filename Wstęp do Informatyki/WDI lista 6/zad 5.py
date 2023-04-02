def generuj_sito(n):
    sito = [True] * n
    sito[0] = False
    sito[1] = False
    for i in range(2,n):
        if sito[i]:
            for j in range(i*i,n,i):
                sito[j] = False
    return sito