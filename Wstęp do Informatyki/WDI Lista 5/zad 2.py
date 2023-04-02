def reprezentacja_silniowa(n):
    a = 1
    i = 0
    while a < n:
        i += 1
        a *= i
    while i > 1:
        a //= i
        print(n // a)
        n = n % a
        i -= 1

reprezentacja_silniowa(100)
