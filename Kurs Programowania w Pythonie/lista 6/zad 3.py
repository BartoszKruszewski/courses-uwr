def czy_pierwsza(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def pierwsze_dzielniki(n):
    for i in range(2,n):
        if n % i == 0 and czy_pierwsza(i):
            print(i)

pierwsze_dzielniki(24)