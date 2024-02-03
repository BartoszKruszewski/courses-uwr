from time import time

def t(n):
    if n == 0:
        return lambda x: 1
    if n == 1:
        return lambda x: x
    return lambda x: 2 * x * t(n - 1)(x) - t(n - 2)(x)

# testy jednostkowe dla t
assert t(2)(2) == 7     # 2x**2 - 1                       # t(2) = 3
assert t(3)(2) == 26    # 4x**3 - 3x                      # t(2) = 26
assert t(4)(2) == 97    # 8x**4 - 8x**2 + 1               # t(2) = 97
assert t(5)(2) == 362   # 16x**5 - 4x**3 - 16x**2 + 5x    # t(2) = 362

def fast_t(n):
    if n == 0:
        return lambda x: 1
    if n == 1:
        return lambda x: x
    k = 2
    while k * k < n:
        if n % k == 0:
            l = n // k
            return lambda x: fast_t(l)(fast_t(k)(x))
        k += 1
    return t(n)

N = 25 # number of tests

# testy poprawnosci dla fast_t, czy odpowiadaja t
for i in range(N):
    assert t(i)(2) == fast_t(i)(2)

# testy szybkosci t
t_times = []
for i in range(N):
    start_time = time()
    t(i)(2)
    end_time = time()
    t_times.append(end_time - start_time)
t_avg_time = sum(t_times) / len(t_times)

# testy szybkosci fast_t
fast_t_times = []
for i in range(N):
    start_time = time()
    fast_t(i)(2)
    end_time = time()
    fast_t_times.append(end_time - start_time)
fast_t_avg_time = sum(fast_t_times) / len(fast_t_times)

print(f't() avg time: {t_avg_time}')
print(f'fast_t() avg time: {fast_t_avg_time}')
print(f'diff (t / fast) * 100%: {t_avg_time * 100 / fast_t_avg_time:.0f}%' )

