def T(n):
    if n == 1: return 1
    else: return T(n-1) + n

print(T(16))