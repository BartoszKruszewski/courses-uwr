from timeit import timeit

def primes_imp(n):
    if n < 2:
        return []
    if n == 2:
        return [2]

    result = [2]
    actual_number = 3
    
    while actual_number <= n:
        k = 2
        good = True
        while k < actual_number:
            if actual_number % k == 0:
                good = False
            k += 1
        if good:
            result.append(actual_number)
        actual_number += 1
    
    return result

def primes_list(n):
    return [
        number for number in range(2, n + 1) 
        if all(number % k != 0 for k in range(2, number))
    ]

def primes_func(n):
    return list(filter(
        lambda number: all(
            map(lambda k: number % k != 0, range(2, number))
        ),
        range(2, n + 1)
    ))

print('  n   imp list func')
for n in range(100, 1000, 100):
    time_imp = timeit('primes_imp(n)', globals = globals(), number=100)
    time_list = timeit('primes_list(n)', globals = globals(), number=100)
    time_func = timeit('primes_func(n)', globals = globals(), number=100)
    print(f'{n}: {time_imp:.2f} {time_list:.2f} {time_func:.2f}')
    