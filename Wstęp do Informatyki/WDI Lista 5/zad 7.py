def najmniejsza_potega(n,m):
    k = 0
    mult = 1
    while mult < m:
        mult *= n
        k += 1
    return k

