S = [-1, 5, -7, 42, 1, 20, 5, 2]

def sum3(s):
    n = len(s)
    s.sort()

    for i in range(n - 2):
        a = s[i]
        start = i + 1
        end = n - 1
        while start < end:
            b = s[start]
            c = s[end]
            if a + b + c == 0:
                return a, b, c
            elif a + b + c > 0:
                end -= 1
            else:
                start += 1

print(*sum3(S))

# złożonośc O(n^2)

# Dowód:

# Obserwacja 1:
# Jeżeli a + b + c > 0 to również a + b + c' > 0, gdzie c' to element na prawo od c.
# Zachodzi to, ponieważ elementy są posortowane.

# Obserwacja 2:
# Jeżeli a + b + c < 0 to również a' + b + c < 0, gdzie a' to element na lewo od a.
# Zachodzi to, ponieważ elementy są posortowane.

# Z tych obserwacji wynika, że nie tracimy potencjalnych rozwiązań sprawdzając rozwiązania naszą wewnętrzną pętla.
# Czyli sprawdzamy kombinacje elementu a ze wszystkimi możliwymi kombinacjami b i c.
# a sprawdzamy dla każdej liczby ze zbioru S, więc sprawdzamy wszystkie możliwości.
