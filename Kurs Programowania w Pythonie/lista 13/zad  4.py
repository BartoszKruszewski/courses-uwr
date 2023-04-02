# zad 5 2017

def prefix(s, t):
    return any(s == t[:i] for i in range(len(t)))

def drabina(L):
    return all(L[i] == L[i-2] for i in range(2,len(L),2)) and all(L[i] == L[i-2] for i in range(3,len(L),2))

def maleRybyWDuzych(L):
    return all(sorted(L, key=len)[i-1] in sorted(L, key=len)[i] for i in range(1,len(L)))

def sumaDlugosciABC(L):
    return sum(len(e) for e in L if all(litera in "abc" for litera in e))

def poltaksowkowa(N):
    return any(N == a**3 + b**3 for a in range(N) for b in range(N))


print(poltaksowkowa(35))
print(sumaDlugosciABC(["baba", "ma", "kota", "a", "ty?"]))
print(maleRybyWDuzych(["rekinisko", "rekin", "eki", "megarekinisko", "megarekiniskozilla"]))

