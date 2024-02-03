def get_w(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    def base(k):
        def function(xi):
            res = 1.0
            for j in range(k):
                res *= (xi - xs[j]) / (xs[k] - xs[j])
            for j in range(k + 1, len(xs)):
                res *= (xi - xs[j]) / (xs[k] - xs[j])
            return res
        return function
    
    return lambda x: sum(ys[k] * base(k)(x) for k in range(len(xs)))