r = 1
n = 1
while r < 10 ** 12:
    n += 1
    r *= n
    print(n, r)

print()

r = 1
n = 1
while r < 10 ** 12:
    n += 1
    r *= n * 2 * 2
    print(n, r)