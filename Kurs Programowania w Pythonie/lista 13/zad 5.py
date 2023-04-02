# zad 5 2019

def zrob_tytul(S):
    return " ".join([s[0].upper() + s[1:] for s in S.split(" ")])

def suma_jednocyfrowyh(L):
    return sum(e for e in L if len(str(e)) == 1)

def same_palindromy(L):
    return all(list(e) == list(reversed(e)) for e in L)

def namiotowa(L):
    def rosnaca(A):
        return all(A[i - 1] < A[i] for i in range(1,len(A)))

    def malejaca(A):
        return all(A[i - 1] > A[i] for i in range(1,len(A)))

    return any(rosnaca(L[:i]) and malejaca(L[i:]) for i in range(len(L)))

def maksymalna_liczba_tekscie(s):
    def tylko_liczby(a):
        return [x for x in "".join(z if z in "0123456789" else " " for z in a).split(" ") if len(x) > 0]

    return max(int(e) for e in tylko_liczby(s))

def wydluzane(L):
    def prefix(s, t):
        return any(s == t[:i] for i in range(len(t)))
    return all(prefix(sorted(L, key=len)[i - 1], sorted(L, key=len)[i]) for i in range(1,len(L)))

print(wydluzane(["abc","ab","a"]))
print(maksymalna_liczba_tekscie("123 hdjfgbbidifgf67huh15 hiub999"))
print(namiotowa([1,2,3,4,5,6,9,3,2,1]))
print(same_palindromy(["aba","okoko","huh"]))
print(suma_jednocyfrowyh([15,35,6,343,78,4,78,5]))
print(zrob_tytul("jakiekolwiek slowa do zamiany"))
