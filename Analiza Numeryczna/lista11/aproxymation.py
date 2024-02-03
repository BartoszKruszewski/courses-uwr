def memoize(f):
    cache = {}
    def memf(*args):
        if args in cache:
            return cache[args]
        res = f(*args)
        cache[args] = res
        return res
    return memf, cache

class Aproxymation:
    def __init__(self, points) -> None:
        self.xs = [p[0] for p in points]
        self.ys = [p[1] for p in points]
        self.p, self.p_cache = memoize(self.new_p)
        self.dot, self.dot_cache = memoize(self.new_dot) # <Pk, Pk>
        self.dotx, self.dotx_cache = memoize(self.new_dotx) # <xPk, Pk>
        self.dotf, self.dotf_cache = memoize(self.new_dotf) # <f, Pk>
        self.c, self.c_cache = memoize(self.new_c) 
        self.d, self.d_cache = memoize(self.new_d) 
        self.a, self.a_cache = memoize(self.new_a)
        self.value, self.value_cache = memoize(self.new_value)

    def new_p(self, k, x):
        if k == 0:
            return 1
        elif k == 1:
            return x - self.c(1)
        return (x - self.c(k)) * self.p(k - 1, x) - self.d(k) * self.p(k - 2, x)

    def new_dot(self, k):
        return sum(self.p(k, x) ** 2 for x in self.xs)

    def new_dotx(self, k):
        return sum(self.p(k, x) ** 2 * x for x in self.xs)

    def new_dotf(self, k):
        return sum(self.p(k, x) * y for x, y in zip(self.xs, self.ys))

    def new_c(self, k):
        return self.dotx(k - 1) / self.dot(k - 1)
    
    def new_d(self, k):
        return self.dot(k - 1) / self.dot(k - 2)
    
    def new_a(self, k):
        return self.dotf(k) / self.dot(k)
    
    def new_value(self, x, n):
        return sum(self.a(k) * self.p(k, x) for k in range(n))

    def clear_cache(self):
        self.p_cache.clear()
        self.dot_cache.clear()
        self.dotx_cache.clear()
        self.dotf_cache.clear()
        self.c_cache.clear()
        self.d_cache.clear()
        self.a_cache.clear()
        self.value_cache.clear()

    def __call__(self, x, n):
        if (x, n - 1) in self.value_cache:
            res = self.value_cache[(x, n - 1)] + self.a(n - 1) * self.p(n - 1, x)
            self.value_cache[(x, n)] = res
            return res
        return self.value(x, n)