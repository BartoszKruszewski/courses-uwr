def test_range(n):
    for i in range(1, n):
        yield i

    for i in (i / n for i in range(1, n)):
        yield i

    for i in range(1, n * n + 1, n):
        yield i

def get_e():
    e = 1
    while 1 + e != 1:
        e /= 10
    return e