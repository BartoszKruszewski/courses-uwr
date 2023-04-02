def generuj_sito(n):
    sito = [True] * n
    sito[0] = False
    sito[1] = False
    for i in range(2,n):
        if sito[i]:
            for j in range(i * i, n, i):
                sito[j] = False
    return sito

def czy_palindrom(n):
    return str(n) == str(n)[::-1]

def palindromy(a,b):
    liczby = []
    k = 0
    sito = generuj_sito(b)
    for i in sito:
        if a <= k <= b:
            if i and czy_palindrom(k):
                liczby.append(k)
        k += 1
    return liczby

print(palindromy(10,1000))

