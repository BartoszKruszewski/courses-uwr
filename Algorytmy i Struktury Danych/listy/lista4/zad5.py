# Pamiętamy jedną kolumną oraz dwie wartości (po lewej oraz po przekątnej).
# W momencie aktualizowania kolumny, wartości które mają zostać nadpisane 
# przenosimy do zmiennych dp[i] -> next -> diagonal.

# Odtwarzanie robimy na podstawie dp, które otrzymamy na końcu. 
# Wystraczy, ze sprawdzimy dla jakich indeksow, dlugosc lcs 
# zostala zwiekszona i otrzymamy nasz podciag. Działa to poniewaz cofając się
# od dp[m] do wartosci wiekszych trafimy na lcs, a w dp po zakonceniu algorytmu
# są wieksze wartosci, inaczjej nie bylyby max i nie zostałyby wzięte.

def lcs(x, y): 
    n = len(x) 
    m = len(y) 

    dp = [0] * (m + 1)
    dp2 = [0] * (n + 1)
    diagonal = 0
    next = 0
    res1 = ""
    res2 = ""

    for i in range(1, n + 1):
        next = 0
        for j in range(1, m + 1):
            diagonal = next
            next = dp[j]
            if x[i - 1] == y[j - 1]:
                dp[j] = diagonal + 1
            else:
                dp[j] = max(dp[j - 1], next)
        dp2[i] = dp[m]

    for j in range(m):
        if dp[j] != dp[j + 1]:
            res1 += y[j]
    for j in range(n):
        if dp2[j] != dp2[j + 1]:
            res2 += x[j]

    a = 0
    b = 0
    while a < dp[m] and b < m:
        if res1[a] == x[b]:
            a += 1
        b += 1
    if a == dp[m]:
        return res1
    else:
        return res2

print(lcs("ralab", "krola"))
print(lcs("krola", "ralab"))

