import random

def randperm(n):
    liczby = list(range(n))
    permutacja = []
    for i in range(n):
        liczba = random.choice(liczby)
        liczby.remove(liczba)
        permutacja.append(liczba)
    return permutacja

for i in range(10):
    print(randperm(10))