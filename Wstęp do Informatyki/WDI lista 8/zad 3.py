def T(n):
    print(n)
    if n == 1: return 1
    else: return 2*T(n/2) + 1

print(T(16))