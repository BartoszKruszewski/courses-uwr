def T(n):
    if n == 1: return 0
    else: return T(n/2) + 1

print(T(16))